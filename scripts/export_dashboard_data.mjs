/**
 * Dependency-free dashboard data exporter.
 *
 * The Python exporter remains the canonical analytics build script. This small
 * companion keeps the interactive React payload refreshable in environments
 * where pandas is not available.
 */
import { readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const rootDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const sourcePath = path.join(rootDir, "data", "processed", "placementlens_students_clean.csv");
const targetPath = path.join(rootDir, "dashboard", "src", "data", "placementData.json");
const skillColumns = ["python_skill", "sql_skill", "excel_skill", "power_bi_skill", "dsa_skill", "cloud_skill", "cybersecurity_skill"];

const median = (values) => {
  const sorted = [...values].sort((a, b) => a - b);
  const middle = Math.floor(sorted.length / 2);
  return sorted.length % 2 ? sorted[middle] : (sorted[middle - 1] + sorted[middle]) / 2;
};

const priCategory = (score) => {
  if (score >= 80) return "High Readiness (80-100)";
  if (score >= 60) return "Moderate (60-79)";
  if (score >= 40) return "Needs Improvement (40-59)";
  return "High Imp. Priority (<40)";
};

const csv = await readFile(sourcePath, "utf8");
const [header, ...rows] = csv.trim().split(/\r?\n/);
const columns = header.split(",");
const students = rows.map((line) => {
  const record = Object.fromEntries(columns.map((column, index) => [column, line.split(",")[index] ?? ""]));
  for (const column of ["cgpa", "internships", "projects", "coding_score", "aptitude_score", "communication_score", "placed", ...skillColumns]) {
    record[column] = Number(record[column]);
  }
  record.package_lpa = record.package_lpa === "" ? null : Number(record.package_lpa);
  record.technical_skill_count = skillColumns.reduce((total, column) => total + record[column], 0);
  record.pri_score = Number((
    0.25 * ((record.technical_skill_count / 7) * 100) +
    0.20 * record.aptitude_score +
    0.15 * ((record.cgpa / 10) * 100) +
    0.15 * ((Math.min(record.projects, 4) / 4) * 100) +
    0.15 * ((Math.min(record.internships, 3) / 3) * 100) +
    0.10 * record.communication_score
  ).toFixed(2));
  record.pri_category = priCategory(record.pri_score);
  return record;
});

const academicScores = students.map((student) => ((student.cgpa / 10) * 100 + student.aptitude_score) / 2);
const practicalScores = students.map((student) => ((student.technical_skill_count / 7) * 100 + student.coding_score) / 2);
const academicMedian = median(academicScores);
const practicalMedian = median(practicalScores);
for (const student of students) {
  const academic = ((student.cgpa / 10) * 100 + student.aptitude_score) / 2;
  const practical = ((student.technical_skill_count / 7) * 100 + student.coding_score) / 2;
  student.prep_quadrant_segment = academic >= academicMedian
    ? (practical >= practicalMedian ? "SEG-Q1" : "SEG-Q3")
    : (practical >= practicalMedian ? "SEG-Q2" : "SEG-Q4");
}

const existing = JSON.parse(await readFile(targetPath, "utf8"));
await writeFile(targetPath, `${JSON.stringify({ insights: existing.insights, students }, null, 2)}\n`);
console.log(`Exported ${students.length} student records to ${targetPath}`);
