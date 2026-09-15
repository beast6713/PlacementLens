import React, { useState } from "react";
import { Code, Brain, GraduationCap, Layers, Sparkles, Search } from "lucide-react";
import { BentoGrid, BentoCard } from "../magicui/BentoGrid";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid, Legend } from "recharts";
import { buildDashboardMetrics } from "../../lib/dashboardMetrics";

export const StudentAnalytics = ({ data, filters, onOpenDetail }) => {
  const { prep_comparison, skill_stats, segments, scopedStudents } = buildDashboardMetrics(data.students, filters);
  const [searchTerm, setSearchTerm] = useState("");

  const prepChartData = [
    {
      metric: "Coding Score (/100)",
      Placed: prep_comparison.coding_score.placed,
      Unplaced: prep_comparison.coding_score.unplaced,
      delta: prep_comparison.coding_score.delta
    },
    {
      metric: "Aptitude Score (/100)",
      Placed: prep_comparison.aptitude_score.placed,
      Unplaced: prep_comparison.aptitude_score.unplaced,
      delta: prep_comparison.aptitude_score.delta
    },
    {
      metric: "CGPA (x10)",
      Placed: prep_comparison.cgpa.placed * 10,
      Unplaced: prep_comparison.cgpa.unplaced * 10,
      delta: prep_comparison.cgpa.delta
    }
  ];

  const filteredStudents = scopedStudents.filter(s => {
    const matchesSearch = s.student_id.toLowerCase().includes(searchTerm.toLowerCase()) || s.branch.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesBranch = filters.branch ? s.branch === filters.branch : true;
    return matchesSearch && matchesBranch;
  });
  const openPreparationDetail = (label, metric) => onOpenDetail({ title: label, kicker: "Preparation comparison", description: "Average preparation score for placed and unplaced students in the active scope.", rows: [{ label: "Placed average", value: metric.placed.toFixed(2) }, { label: "Unplaced average", value: metric.unplaced.toFixed(2) }, { label: "Placed delta", value: `${metric.delta >= 0 ? "+" : ""}${metric.delta.toFixed(2)}` }] });

  return (
    <div className="space-y-6 animate-fadeIn">
      {/* Header */}
      <div>
        <h1 className="text-2xl md:text-3xl font-bold text-white flex items-center gap-3">
          <span className="p-2 rounded-xl bg-cyan-500/10 text-cyan-400 border border-cyan-500/30">02</span>
          Student & Placement Analytics
        </h1>
        <p className="text-slate-400 text-sm mt-1">
          Preparation profiles, technical skill coverage, skill placement spreads, and preparation quadrants
        </p>
      </div>

      {/* Preparation Profile Deltas */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="glass-card detail-trigger p-4 rounded-xl border border-slate-800" role="button" tabIndex={0} onClick={() => openPreparationDetail("Coding score", prep_comparison.coding_score)}>
          <div className="flex items-center gap-2 text-cyan-400 mb-2">
            <Code className="w-5 h-5" />
            <span className="text-xs font-semibold uppercase">Coding Score</span>
          </div>
          <div className="text-2xl font-bold text-white">{prep_comparison.coding_score.placed.toFixed(2)} vs {prep_comparison.coding_score.unplaced.toFixed(2)}</div>
          <div className="text-xs text-emerald-400 font-medium mt-1">{prep_comparison.coding_score.delta >= 0 ? "+" : ""}{prep_comparison.coding_score.delta.toFixed(2)} pts Placed Delta</div>
        </div>

        <div className="glass-card detail-trigger p-4 rounded-xl border border-slate-800" role="button" tabIndex={0} onClick={() => openPreparationDetail("Aptitude score", prep_comparison.aptitude_score)}>
          <div className="flex items-center gap-2 text-indigo-400 mb-2">
            <Brain className="w-5 h-5" />
            <span className="text-xs font-semibold uppercase">Aptitude Score</span>
          </div>
          <div className="text-2xl font-bold text-white">{prep_comparison.aptitude_score.placed.toFixed(2)} vs {prep_comparison.aptitude_score.unplaced.toFixed(2)}</div>
          <div className="text-xs text-emerald-400 font-medium mt-1">{prep_comparison.aptitude_score.delta >= 0 ? "+" : ""}{prep_comparison.aptitude_score.delta.toFixed(2)} pts Placed Delta</div>
        </div>

        <div className="glass-card detail-trigger p-4 rounded-xl border border-slate-800" role="button" tabIndex={0} onClick={() => openPreparationDetail("Average CGPA", prep_comparison.cgpa)}>
          <div className="flex items-center gap-2 text-amber-400 mb-2">
            <GraduationCap className="w-5 h-5" />
            <span className="text-xs font-semibold uppercase">Average CGPA</span>
          </div>
          <div className="text-2xl font-bold text-white">{prep_comparison.cgpa.placed.toFixed(2)} vs {prep_comparison.cgpa.unplaced.toFixed(2)}</div>
          <div className="text-xs text-emerald-400 font-medium mt-1">{prep_comparison.cgpa.delta >= 0 ? "+" : ""}{prep_comparison.cgpa.delta.toFixed(2)} CGPA Placed Delta</div>
        </div>

        <div className="glass-card detail-trigger p-4 rounded-xl border border-slate-800" role="button" tabIndex={0} onClick={() => onOpenDetail({ title: "Technical skill count", kicker: "Preparation comparison", description: "Median number of technical skills in the active scope.", rows: [{ label: "Placed median", value: prep_comparison.technical_skill_count.placed_median }, { label: "Unplaced median", value: prep_comparison.technical_skill_count.unplaced_median }, { label: "Difference", value: prep_comparison.technical_skill_count.delta }] })}>
          <div className="flex items-center gap-2 text-pink-400 mb-2">
            <Layers className="w-5 h-5" />
            <span className="text-xs font-semibold uppercase">Tech Skill Median</span>
          </div>
          <div className="text-2xl font-bold text-white">{prep_comparison.technical_skill_count.placed_median} vs {prep_comparison.technical_skill_count.unplaced_median} Skills</div>
          <div className="text-xs text-emerald-400 font-medium mt-1">{prep_comparison.technical_skill_count.delta >= 0 ? "+" : ""}{prep_comparison.technical_skill_count.delta} Skill Placed Delta</div>
        </div>
      </div>

      {/* Magic UI BentoGrid for Skill Placement Spreads */}
      <div>
        <h2 className="text-lg font-bold text-white mb-3 flex items-center gap-2">
          <Sparkles className="w-5 h-5 text-cyan-400" />
          Technical Skill Placement Signals (Observed Spreads)
        </h2>
        <BentoGrid className="auto-rows-[13rem]">
          {skill_stats.slice(0, 3).map((skill, idx) => (
            <BentoCard
              key={idx}
              name={`${skill.skill_name} Skill`}
              Icon={Sparkles}
              description={`Holder Prevalence: ${skill.holder_pct}% (${skill.holder_count} students)`}
              onClick={() => onOpenDetail({ title: `${skill.skill_name} skill signal`, kicker: "Skill detail", description: "Observed placement comparison for students with and without this skill.", rows: [{ label: "Skill holders", value: `${skill.holder_count} (${skill.holder_pct}%)` }, { label: "Holder placement rate", value: `${skill.skill_placement_rate}%` }, { label: "Non-holder placement rate", value: `${skill.no_skill_placement_rate}%` }, { label: "Observed spread", value: `${skill.spread} pp` }] })}
            >
              <div className="mt-2 space-y-2">
                <div className="flex justify-between items-center text-sm">
                  <span className="text-slate-400">Skill Placement Rate:</span>
                  <span className="text-emerald-400 font-bold text-base">{skill.skill_placement_rate}%</span>
                </div>
                <div className="flex justify-between items-center text-sm">
                  <span className="text-slate-400">Non-Holder Rate:</span>
                  <span className="text-slate-300 font-medium">{skill.no_skill_placement_rate}%</span>
                </div>
                <div className="mt-3 p-2 rounded-lg bg-cyan-500/10 border border-cyan-500/20 text-cyan-300 text-xs font-bold text-center">
                  +{skill.spread} pp Placement Advantage
                </div>
              </div>
            </BentoCard>
          ))}
        </BentoGrid>
      </div>

      {/* Quadrant Preparation Segments */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="glass-panel p-6 rounded-2xl">
          <h2 className="text-lg font-bold text-white mb-1">Preparation Quadrants</h2>
          <p className="text-xs text-slate-400 mb-4">Phase 4 pre-outcome median split preparation segments</p>

          <div className="grid grid-cols-2 gap-3">
            {segments.map((seg, idx) => (
              <div key={idx} className="glass-card detail-trigger p-4 rounded-xl border border-slate-800" role="button" tabIndex={0} onClick={() => onOpenDetail({ title: seg.name, kicker: "Preparation segment", description: "Students grouped using the dashboard's preparation quadrant framework.", rows: [{ label: "Students", value: seg.count }, { label: "Placement rate", value: `${seg.placement_rate}%` }] })}>
                <div className="text-xs font-bold text-cyan-400 mb-1">{seg.segment_id}</div>
                <div className="text-sm font-semibold text-white truncate">{seg.name.split(':')[1]}</div>
                <div className="mt-2 text-xs text-slate-400">
                  <span>Count: <strong className="text-white">{seg.count}</strong></span>
                </div>
                <div className="text-xs font-bold text-emerald-400 mt-1">
                  {seg.placement_rate}% Placed
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Prep Comparison Bar Chart */}
        <div className="glass-panel detail-trigger p-6 rounded-2xl" role="button" tabIndex={0} onClick={() => onOpenDetail({ title: "Preparation benchmark", kicker: "Chart detail", description: "Average pre-placement score comparison in the active scope.", rows: [{ label: "Coding", value: `${prep_comparison.coding_score.placed} vs ${prep_comparison.coding_score.unplaced}` }, { label: "Aptitude", value: `${prep_comparison.aptitude_score.placed} vs ${prep_comparison.aptitude_score.unplaced}` }, { label: "CGPA", value: `${prep_comparison.cgpa.placed} vs ${prep_comparison.cgpa.unplaced}` }] })}>
          <h2 className="text-lg font-bold text-white mb-1">Preparation Benchmark</h2>
          <p className="text-xs text-slate-400 mb-4">Average scores comparison between Placed and Unplaced cohorts</p>

          <div className="h-56 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={prepChartData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1E293B" />
                <XAxis dataKey="metric" stroke="#94A3B8" fontSize={11} />
                <YAxis stroke="#64748B" fontSize={11} />
                <Tooltip contentStyle={{ backgroundColor: "#0F172A", borderColor: "#334155", borderRadius: "12px", color: "#F8FAFC" }} />
                <Legend />
                <Bar dataKey="Placed" fill="#10B981" radius={[4, 4, 0, 0]} />
                <Bar dataKey="Unplaced" fill="#F59E0B" radius={[4, 4, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {/* Student Data Directory Table */}
      <div className="glass-panel rounded-2xl p-6 space-y-4">
        <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
          <div>
            <h2 className="text-lg font-bold text-white">Student Preparation Directory</h2>
            <p className="text-xs text-slate-400">Exploratory preparation profiles ({filteredStudents.length} students in the active scope)</p>
          </div>

          <div className="relative w-full md:w-64">
            <Search className="w-4 h-4 absolute left-3 top-3 text-slate-400" />
            <input
              type="text"
              placeholder="Search Student ID or Branch..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full bg-slate-900 border border-slate-800 rounded-xl pl-9 pr-4 py-2 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-cyan-500"
            />
          </div>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-300">
            <thead className="bg-slate-900/80 text-slate-400 font-bold uppercase tracking-wider border-b border-slate-800">
              <tr>
                <th className="py-3 px-4">Student ID</th>
                <th className="py-3 px-4">Branch</th>
                <th className="py-3 px-4">CGPA</th>
                <th className="py-3 px-4">Coding</th>
                <th className="py-3 px-4">Aptitude</th>
                <th className="py-3 px-4">Tech Skills</th>
                <th className="py-3 px-4">PRI Score</th>
                <th className="py-3 px-4">PRI Tier</th>
                <th className="py-3 px-4">Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60">
              {filteredStudents.slice(0, 10).map((st, idx) => (
                <tr key={idx} onClick={() => onOpenDetail({ title: st.student_id, kicker: "Student profile", description: `Detailed preparation and placement record for a ${st.branch} student.`, rows: [{ label: "CGPA", value: st.cgpa }, { label: "Coding score", value: st.coding_score }, { label: "Aptitude score", value: st.aptitude_score }, { label: "Technical skills", value: `${st.technical_skill_count} / 7` }, { label: "PRI score", value: st.pri_score }, { label: "Placement status", value: st.placed === 1 ? `Placed · ${st.company_type} · ₹${st.package_lpa} LPA` : "Unplaced" }] })} className="detail-trigger hover:bg-slate-800/40 transition-colors">
                  <td className="py-3 px-4 font-bold text-cyan-400">{st.student_id}</td>
                  <td className="py-3 px-4">{st.branch}</td>
                  <td className="py-3 px-4 font-semibold">{st.cgpa}</td>
                  <td className="py-3 px-4">{st.coding_score}</td>
                  <td className="py-3 px-4">{st.aptitude_score}</td>
                  <td className="py-3 px-4">{st.technical_skill_count} / 7</td>
                  <td className="py-3 px-4 font-bold text-white">{st.pri_score}</td>
                  <td className="py-3 px-4">
                    <span className="bg-slate-800 text-slate-300 px-2 py-0.5 rounded text-[10px]">
                      {st.pri_category.split(' ')[0]}
                    </span>
                  </td>
                  <td className="py-3 px-4">
                    {st.placed === 1 ? (
                      <span className="bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 px-2 py-0.5 rounded text-[10px] font-bold">
                        Placed ({st.company_type})
                      </span>
                    ) : (
                      <span className="bg-amber-500/10 text-amber-400 border border-amber-500/30 px-2 py-0.5 rounded text-[10px] font-bold">
                        Unplaced
                      </span>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
