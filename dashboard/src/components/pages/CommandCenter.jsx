import React from "react";
import { Users, UserCheck, UserX, DollarSign, Award, ArrowUpRight, CheckCircle2 } from "lucide-react";
import { BorderBeam } from "../magicui/BorderBeam";
import { NumberTicker } from "../magicui/NumberTicker";
import { MagicMarquee } from "../magicui/MagicMarquee";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell } from "recharts";
import { buildDashboardMetrics } from "../../lib/dashboardMetrics";

export const CommandCenter = ({ data, filters, onOpenDetail }) => {
  const { metadata, branch_stats, pri_tiers, skill_stats } = buildDashboardMetrics(data.students, filters);
  const leadingBranch = [...branch_stats].sort((a, b) => b.rate - a.rate)[0];
  const cohortLabel = filters.branch || "All Branches";
  const openMetric = (title, value, description, rows = []) => onOpenDetail({ title, kicker: "Command center metric", description, rows: [{ label: "Current value", value }, ...rows], note: `Scope: ${cohortLabel}` });

  const branchColors = {
    CE: "#00F0FF",
    EEE: "#3B82F6",
    IT: "#6366F1",
    CSE: "#8B5CF6",
    ECE: "#EC4899",
    ME: "#F59E0B"
  };

  return (
    <div className="space-y-6 animate-fadeIn">
      {/* Page Title & Subtitle */}
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 className="text-2xl md:text-3xl font-bold text-white flex items-center gap-3">
            <span className="p-2 rounded-xl bg-cyan-500/10 text-cyan-400 border border-cyan-500/30">01</span>
            Command Center
          </h1>
          <p className="text-slate-400 text-sm mt-1">
            Macro placement outcome overview and institutional readiness benchmark
          </p>
        </div>

        {/* Live Filter Indicator Badge */}
        <div className="flex items-center gap-2 text-xs bg-slate-900/80 px-3 py-1.5 rounded-full border border-slate-800">
          <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
          <span className="text-slate-300 font-medium">Cohort Scope:</span>
          <span className="text-cyan-400 font-bold">{cohortLabel}</span>
        </div>
      </div>

      {/* Hero KPI Cards with Magic UI BorderBeam & NumberTicker */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {/* KPI 1: Total Students */}
        <div className="relative glass-card detail-trigger rounded-2xl p-5 overflow-hidden" role="button" tabIndex={0} onClick={() => openMetric("Total students", metadata.total_students.toLocaleString(), "Students matching the current shared filters.", [{ label: "Placed", value: metadata.placed_students }, { label: "Unplaced", value: metadata.unplaced_students }])} onKeyDown={(event) => event.key === "Enter" && openMetric("Total students", metadata.total_students.toLocaleString(), "Students matching the current shared filters.") }>
          <BorderBeam size={180} duration={10} colorFrom="#00F0FF" colorTo="#3B82F6" />
          <div className="flex justify-between items-start mb-3">
            <span className="text-slate-400 text-xs font-medium uppercase tracking-wider">Total Students</span>
            <div className="p-2 rounded-xl bg-slate-800/80 text-cyan-400">
              <Users className="w-5 h-5" />
            </div>
          </div>
          <div className="text-3xl font-extrabold text-white">
            <NumberTicker value={metadata.total_students} />
          </div>
          <div className="mt-2 flex items-center text-xs text-slate-400 gap-1">
            <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
            <span>Active filter scope</span>
          </div>
        </div>

        {/* KPI 2: Placed Students */}
        <div className="relative glass-card detail-trigger rounded-2xl p-5 overflow-hidden" role="button" tabIndex={0} onClick={() => openMetric("Placement outcome", `${metadata.placement_rate}%`, "Placement performance for the students currently in view.", [{ label: "Placed students", value: metadata.placed_students }, { label: "Total students", value: metadata.total_students }])}>
          <BorderBeam size={180} duration={12} delay={3} colorFrom="#10B981" colorTo="#00F0FF" />
          <div className="flex justify-between items-start mb-3">
            <span className="text-slate-400 text-xs font-medium uppercase tracking-wider">Placed Students</span>
            <div className="p-2 rounded-xl bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
              <UserCheck className="w-5 h-5" />
            </div>
          </div>
          <div className="text-3xl font-extrabold text-emerald-400">
            <NumberTicker value={metadata.placed_students} />
          </div>
          <div className="mt-2 flex items-center text-xs text-emerald-400 font-semibold gap-1">
            <ArrowUpRight className="w-3.5 h-3.5" />
            <span>{metadata.placement_rate}% Rate</span>
          </div>
        </div>

        {/* KPI 3: Unplaced Students */}
        <div className="relative glass-card detail-trigger rounded-2xl p-5 overflow-hidden" role="button" tabIndex={0} onClick={() => openMetric("Students needing placement support", metadata.unplaced_students.toLocaleString(), "Students without a recorded placement in the active scope.", [{ label: "Improvement opportunity", value: `${(100 - metadata.placement_rate).toFixed(2)}%` }])}>
          <div className="flex justify-between items-start mb-3">
            <span className="text-slate-400 text-xs font-medium uppercase tracking-wider">Unplaced Students</span>
            <div className="p-2 rounded-xl bg-amber-500/10 text-amber-400 border border-amber-500/20">
              <UserX className="w-5 h-5" />
            </div>
          </div>
          <div className="text-3xl font-extrabold text-amber-400">
            <NumberTicker value={metadata.unplaced_students} />
          </div>
          <div className="mt-2 text-xs text-slate-400">
            <span>{metadata.total_students ? `${(100 - metadata.placement_rate).toFixed(2)}% Improvement Opportunity` : "No students in scope"}</span>
          </div>
        </div>

        {/* KPI 4: Average Package */}
        <div className="relative glass-card detail-trigger rounded-2xl p-5 overflow-hidden" role="button" tabIndex={0} onClick={() => openMetric("Average package", `₹${metadata.mean_package} LPA`, "Average compensation among placed students only.", [{ label: "Median", value: `₹${metadata.median_package} LPA` }, { label: "Interquartile range", value: `₹${metadata.iqr_package} LPA` }])}>
          <BorderBeam size={180} duration={14} delay={6} colorFrom="#6366F1" colorTo="#EC4899" />
          <div className="flex justify-between items-start mb-3">
            <span className="text-slate-400 text-xs font-medium uppercase tracking-wider">Average Package</span>
            <div className="p-2 rounded-xl bg-indigo-500/10 text-indigo-400 border border-indigo-500/20">
              <DollarSign className="w-5 h-5" />
            </div>
          </div>
          <div className="text-3xl font-extrabold text-white">
            <NumberTicker value={metadata.mean_package} decimalPlaces={2} prefix="₹" suffix=" LPA" />
          </div>
          <div className="mt-2 text-xs text-slate-400 flex justify-between">
            <span>Median: ₹{metadata.median_package} LPA</span>
            <span className="text-indigo-400">IQR: {metadata.iqr_package} LPA</span>
          </div>
        </div>
      </div>

      {/* Magic Marquee Ticker of Key Skill Signals */}
      <div className="glass-card rounded-xl py-2 px-3 overflow-hidden border border-slate-800">
        <div className="flex items-center gap-3">
          <span className="text-xs font-bold uppercase tracking-wider text-cyan-400 bg-cyan-500/10 px-2.5 py-1 rounded-md border border-cyan-500/30 whitespace-nowrap">
            Skill Signals
          </span>
          <MagicMarquee pauseOnHover className="[--duration:25s]">
            {skill_stats.map((skill, idx) => (
              <button key={idx} onClick={() => onOpenDetail({ title: `${skill.skill_name} placement signal`, kicker: "Skill detail", description: "Observed placement rate comparison for students with and without this skill.", rows: [{ label: "Skill holders", value: `${skill.holder_count} (${skill.holder_pct}%)` }, { label: "Holder placement rate", value: `${skill.skill_placement_rate}%` }, { label: "Non-holder placement rate", value: `${skill.no_skill_placement_rate}%` }, { label: "Observed spread", value: `${skill.spread} pp` }] })} className="flex items-center gap-2 bg-slate-900/60 px-3 py-1 rounded-lg text-xs border border-slate-800 whitespace-nowrap">
                <span className="font-semibold text-white">{skill.skill_name}:</span>
                <span className="text-emerald-400 font-bold">+{skill.spread} pp spread</span>
                <span className="text-slate-500">({skill.skill_placement_rate}% placed)</span>
              </button>
            ))}
          </MagicMarquee>
        </div>
      </div>

      {/* Main Charts Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Branch Placement Rates Chart */}
        <div className="lg:col-span-2 glass-panel detail-trigger rounded-2xl p-6 relative" role="button" tabIndex={0} onClick={() => onOpenDetail({ title: "Branch placement benchmark", kicker: "Chart detail", description: "Compare placement outcomes across the branches currently included in the active scope.", rows: branch_stats.map((branch) => ({ label: branch.branch, value: `${branch.rate}% · ${branch.placed}/${branch.total} placed` })) })}>
          <div className="flex justify-between items-center mb-6">
            <div>
              <h2 className="text-lg font-bold text-white">Branch Placement Benchmark</h2>
              <p className="text-xs text-slate-400">Placement rate comparison within the active filter scope</p>
            </div>
            <span className="text-xs text-cyan-400 font-medium bg-cyan-500/10 px-2.5 py-1 rounded-lg border border-cyan-500/20">
              {leadingBranch ? `${leadingBranch.branch} Leader: ${leadingBranch.rate}%` : "No branch data"}
            </span>
          </div>

          <div className="h-64 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={branch_stats} layout="vertical" margin={{ top: 5, right: 30, left: 10, bottom: 5 }}>
                <XAxis type="number" domain={[0, 100]} unit="%" stroke="#64748B" fontSize={12} />
                <YAxis dataKey="branch" type="category" stroke="#94A3B8" fontSize={12} fontWeight="bold" />
                <Tooltip
                  contentStyle={{ backgroundColor: "#0F172A", borderColor: "#334155", borderRadius: "12px", color: "#F8FAFC" }}
                  formatter={(value, name, props) => [`${value}% (${props.payload.placed}/${props.payload.total})`, "Placement Rate"]}
                />
                <Bar dataKey="rate" radius={[0, 8, 8, 0]} onClick={(entry) => entry?.payload && onOpenDetail({ title: `${entry.payload.branch} placement rate`, kicker: "Branch detail", description: "Placement outcome for this department in the active filter scope.", rows: [{ label: "Placement rate", value: `${entry.payload.rate}%` }, { label: "Placed", value: entry.payload.placed }, { label: "Unplaced", value: entry.payload.unplaced }, { label: "Total", value: entry.payload.total }, { label: "Average package", value: `₹${entry.payload.avg_package} LPA` }] })}>
                  {branch_stats.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={branchColors[entry.branch] || "#3B82F6"} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* PRI Tier Breakdown Panel */}
        <div className="glass-panel rounded-2xl p-6 relative">
          <div className="flex items-center gap-2 mb-4">
            <Award className="w-5 h-5 text-indigo-400" />
            <h2 className="text-lg font-bold text-white">Readiness Index Tiers</h2>
          </div>
          <p className="text-xs text-slate-400 mb-4">
            Phase 4 Placement Readiness Index (PRI 0–100) distribution across cohort
          </p>

          <div className="space-y-4">
            {pri_tiers.map((tier, idx) => (
              <button key={idx} onClick={() => onOpenDetail({ title: tier.tier, kicker: "Readiness tier", description: "Students assigned to this Placement Readiness Index tier in the active scope.", rows: [{ label: "Students", value: tier.count }, { label: "Placement rate", value: `${tier.placement_rate}%` }] })} className="space-y-1.5 w-full text-left">
                <div className="flex justify-between text-xs font-semibold">
                  <span className="text-slate-300">{tier.tier}</span>
                  <span className="text-cyan-400 font-bold">{tier.count} students ({tier.placement_rate}% placed)</span>
                </div>
                <div className="w-full h-2 bg-slate-900 rounded-full overflow-hidden border border-slate-800">
                  <div
                    className="h-full rounded-full transition-all duration-1000 bg-gradient-to-r from-cyan-500 to-indigo-500"
                    style={{ width: `${(tier.count / metadata.total_students) * 100}%` }}
                  />
                </div>
              </button>
            ))}
          </div>

          <div className="mt-6 p-3 rounded-xl bg-slate-900/60 border border-slate-800/80 text-xs text-slate-400">
            <span className="font-bold text-white">PRI Standard:</span> 25% Tech + 20% Aptitude + 15% CGPA + 15% Projects + 15% Internships + 10% Comm. Zero target outcome leakage.
          </div>
        </div>
      </div>
    </div>
  );
};
