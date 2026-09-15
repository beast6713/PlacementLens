const BRANCHES = ["CE", "EEE", "IT", "CSE", "ECE", "ME"];

const SKILLS = [
  ["sql_skill", "SQL"],
  ["python_skill", "Python"],
  ["cloud_skill", "Cloud"],
  ["dsa_skill", "DSA"],
  ["cybersecurity_skill", "Cybersecurity"],
  ["power_bi_skill", "Power BI"],
  ["excel_skill", "Excel"],
];

const median = (values) => {
  if (!values.length) return 0;
  const sorted = [...values].sort((a, b) => a - b);
  const middle = Math.floor(sorted.length / 2);
  return sorted.length % 2 ? sorted[middle] : (sorted[middle - 1] + sorted[middle]) / 2;
};

const round = (value) => Number(value.toFixed(2));
const rate = (placed, total) => (total ? round((placed / total) * 100) : 0);
const average = (values) => (values.length ? round(values.reduce((sum, value) => sum + value, 0) / values.length) : 0);

export const filterStudents = (students, filters) => students.filter((student) =>
  (!filters.branch || student.branch === filters.branch) &&
  (!filters.gender || student.gender === filters.gender) &&
  (!filters.placed || String(student.placed) === filters.placed)
);

export const buildDashboardMetrics = (students, filters) => {
  const scopedStudents = filterStudents(students || [], filters);
  const placedStudents = scopedStudents.filter((student) => student.placed === 1);
  const unplacedStudents = scopedStudents.filter((student) => student.placed === 0);
  const packages = placedStudents
    .map((student) => Number(student.package_lpa))
    .filter(Number.isFinite);
  const sortedPackages = [...packages].sort((a, b) => a - b);
  const lowerHalf = sortedPackages.slice(0, Math.floor(sortedPackages.length / 2));
  const upperHalf = sortedPackages.slice(Math.ceil(sortedPackages.length / 2));

  const metadata = {
    total_students: scopedStudents.length,
    placed_students: placedStudents.length,
    unplaced_students: unplacedStudents.length,
    placement_rate: rate(placedStudents.length, scopedStudents.length),
    mean_package: average(packages),
    median_package: round(median(packages)),
    iqr_package: round(median(upperHalf) - median(lowerHalf)),
  };

  const branch_stats = BRANCHES.map((branch) => {
    const branchStudents = scopedStudents.filter((student) => student.branch === branch);
    const branchPlaced = branchStudents.filter((student) => student.placed === 1);
    const branchPackages = branchPlaced.map((student) => Number(student.package_lpa)).filter(Number.isFinite);
    return {
      branch,
      total: branchStudents.length,
      placed: branchPlaced.length,
      unplaced: branchStudents.length - branchPlaced.length,
      rate: rate(branchPlaced.length, branchStudents.length),
      avg_package: average(branchPackages),
    };
  }).filter((branch) => branch.total > 0);

  const company_stats = ["Product", "Startup", "Service", "Other"].map((company_type) => {
    const companyStudents = placedStudents.filter((student) => student.company_type === company_type);
    const companyPackages = companyStudents.map((student) => Number(student.package_lpa)).filter(Number.isFinite);
    return {
      company_type,
      count: companyStudents.length,
      share_pct: rate(companyStudents.length, placedStudents.length),
      mean_package: average(companyPackages),
      median_package: round(median(companyPackages)),
    };
  }).filter((company) => company.count > 0);

  const comparison = (field) => {
    const placedValues = placedStudents.map((student) => Number(student[field])).filter(Number.isFinite);
    const unplacedValues = unplacedStudents.map((student) => Number(student[field])).filter(Number.isFinite);
    const placed = average(placedValues);
    const unplaced = average(unplacedValues);
    return { placed, unplaced, delta: round(placed - unplaced) };
  };
  const prep_comparison = {
    coding_score: comparison("coding_score"),
    aptitude_score: comparison("aptitude_score"),
    cgpa: comparison("cgpa"),
    technical_skill_count: {
      placed_median: round(median(placedStudents.map((student) => Number(student.technical_skill_count)).filter(Number.isFinite))),
      unplaced_median: round(median(unplacedStudents.map((student) => Number(student.technical_skill_count)).filter(Number.isFinite))),
      delta: 0,
    },
  };
  prep_comparison.technical_skill_count.delta = round(
    prep_comparison.technical_skill_count.placed_median - prep_comparison.technical_skill_count.unplaced_median
  );

  const skill_stats = SKILLS.map(([skill_key, skill_name]) => {
    const holders = scopedStudents.filter((student) => Number(student[skill_key]) === 1);
    const nonHolders = scopedStudents.filter((student) => Number(student[skill_key]) === 0);
    const holderRate = rate(holders.filter((student) => student.placed === 1).length, holders.length);
    const noSkillRate = rate(nonHolders.filter((student) => student.placed === 1).length, nonHolders.length);
    return {
      skill_key,
      skill_name,
      holder_count: holders.length,
      holder_pct: rate(holders.length, scopedStudents.length),
      skill_placement_rate: holderRate,
      no_skill_placement_rate: noSkillRate,
      spread: round(holderRate - noSkillRate),
    };
  }).sort((a, b) => b.spread - a.spread);

  const tierDefinitions = [
    ["High Readiness (80-100)", (score) => score >= 80],
    ["Moderate (60-79)", (score) => score >= 60 && score < 80],
    ["Needs Improvement (40-59)", (score) => score >= 40 && score < 60],
    ["High Imp. Priority (<40)", (score) => score < 40],
  ];
  const pri_tiers = tierDefinitions.map(([tier, matches]) => {
    const tierStudents = scopedStudents.filter((student) => matches(Number(student.pri_score)));
    return { tier, count: tierStudents.length, placement_rate: rate(tierStudents.filter((student) => student.placed === 1).length, tierStudents.length) };
  });

  const segmentDefinitions = [
    ["SEG-Q1", "Q1: Balanced High Achievers"],
    ["SEG-Q2", "Q2: Practical Builders"],
    ["SEG-Q3", "Q3: Academic Focus"],
    ["SEG-Q4", "Q4: Comprehensive Imp. Priority"],
  ];
  const segments = segmentDefinitions.map(([segment_id, name]) => {
    const segmentStudents = scopedStudents.filter((student) => student.prep_quadrant_segment === segment_id);
    return { segment_id, name, count: segmentStudents.length, placement_rate: rate(segmentStudents.filter((student) => student.placed === 1).length, segmentStudents.length) };
  });

  return { scopedStudents, metadata, branch_stats, company_stats, prep_comparison, skill_stats, pri_tiers, segments };
};
