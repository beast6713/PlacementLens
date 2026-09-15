import React from "react";
import { Building2, ShieldAlert } from "lucide-react";
import { BorderBeam } from "../magicui/BorderBeam";
import { NumberTicker } from "../magicui/NumberTicker";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid, Cell } from "recharts";
import { buildDashboardMetrics } from "../../lib/dashboardMetrics";

export const CompanyIntelligence = ({ data, filters, onOpenDetail }) => {
  const { metadata, company_stats, branch_stats } = buildDashboardMetrics(data.students, filters);

  const companyColors = {
    Product: "#00F0FF",
    Startup: "#6366F1",
    Service: "#3B82F6",
    Other: "#F59E0B"
  };

  return (
    <div className="space-y-6 animate-fadeIn">
      {/* Header */}
      <div>
        <h1 className="text-2xl md:text-3xl font-bold text-white flex items-center gap-3">
          <span className="p-2 rounded-xl bg-cyan-500/10 text-cyan-400 border border-cyan-500/30">03</span>
          Company & Package Intelligence
        </h1>
        <p className="text-slate-400 text-sm mt-1">
          Placed student compensation distributions and company-type tier analysis for the active filter scope
        </p>
      </div>

      {/* Package Headline KPI Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <div className="glass-card detail-trigger p-5 rounded-2xl border border-slate-800" role="button" tabIndex={0} onClick={() => onOpenDetail({ title: "Placed student cohort", kicker: "Package detail", description: "Students in the active scope with a recorded placement.", rows: [{ label: "Placed students", value: metadata.placed_students }, { label: "Placement rate", value: `${metadata.placement_rate}%` }] })}>
          <div className="text-slate-400 text-xs font-semibold uppercase tracking-wider mb-2">Placed Student Cohort</div>
          <div className="text-3xl font-extrabold text-emerald-400">
            <NumberTicker value={metadata.placed_students} />
          </div>
          <div className="text-xs text-slate-400 mt-1">Within active filter scope</div>
        </div>

        <div className="relative glass-card detail-trigger p-5 rounded-2xl overflow-hidden border border-slate-800" role="button" tabIndex={0} onClick={() => onOpenDetail({ title: "Mean package", kicker: "Package detail", description: "Arithmetic mean for placed-student compensation only.", rows: [{ label: "Mean", value: `₹${metadata.mean_package} LPA` }, { label: "Placed students", value: metadata.placed_students }] })}>
          <BorderBeam size={160} duration={10} colorFrom="#00F0FF" colorTo="#3B82F6" />
          <div className="text-slate-400 text-xs font-semibold uppercase tracking-wider mb-2">Placed Package Mean</div>
          <div className="text-3xl font-extrabold text-white">
            <NumberTicker value={metadata.mean_package} decimalPlaces={2} prefix="₹" suffix=" LPA" />
          </div>
          <div className="text-xs text-cyan-400 mt-1">Arithmetic Compensation Mean</div>
        </div>

        <div className="glass-card detail-trigger p-5 rounded-2xl border border-slate-800" role="button" tabIndex={0} onClick={() => onOpenDetail({ title: "Median package", kicker: "Package detail", description: "The midpoint of placed-student compensation, less affected by outliers.", rows: [{ label: "Median", value: `₹${metadata.median_package} LPA` }, { label: "Mean", value: `₹${metadata.mean_package} LPA` }] })}>
          <div className="text-slate-400 text-xs font-semibold uppercase tracking-wider mb-2">Placed Package Median</div>
          <div className="text-3xl font-extrabold text-indigo-400">
            <NumberTicker value={metadata.median_package} decimalPlaces={2} prefix="₹" suffix=" LPA" />
          </div>
          <div className="text-xs text-slate-400 mt-1">Robust Skew-Resistant Median</div>
        </div>

        <div className="glass-card detail-trigger p-5 rounded-2xl border border-slate-800" role="button" tabIndex={0} onClick={() => onOpenDetail({ title: "Package spread", kicker: "Package detail", description: "Interquartile range: the spread of the middle 50% of placed packages.", rows: [{ label: "IQR", value: `₹${metadata.iqr_package} LPA` }] })}>
          <div className="text-slate-400 text-xs font-semibold uppercase tracking-wider mb-2">Package IQR</div>
          <div className="text-3xl font-extrabold text-pink-400">
            <NumberTicker value={metadata.iqr_package} decimalPlaces={2} prefix="₹" suffix=" LPA" />
          </div>
          <div className="text-xs text-slate-400 mt-1">Interquartile Range Spread</div>
        </div>
      </div>

      {/* Company Type Compensation Cards */}
      <div>
        <h2 className="text-lg font-bold text-white mb-3 flex items-center gap-2">
          <Building2 className="w-5 h-5 text-cyan-400" />
          Company Type Compensation Tiers
        </h2>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {company_stats.map((comp, idx) => (
            <div key={idx} className="glass-card detail-trigger p-5 rounded-2xl relative overflow-hidden border border-slate-800 hover:border-cyan-500/40" role="button" tabIndex={0} onClick={() => onOpenDetail({ title: `${comp.company_type} companies`, kicker: "Company tier detail", description: "Placed-student compensation for this company classification.", rows: [{ label: "Placed students", value: comp.count }, { label: "Share of placements", value: `${comp.share_pct}%` }, { label: "Mean package", value: `₹${comp.mean_package} LPA` }, { label: "Median package", value: `₹${comp.median_package} LPA` }] })}>
              <div className="flex justify-between items-center mb-3">
                <span className="text-sm font-bold text-white">{comp.company_type}</span>
                <span className="text-xs bg-slate-800 text-cyan-400 px-2.5 py-0.5 rounded-full font-semibold">
                  {comp.count} Placed
                </span>
              </div>

              <div className="space-y-2">
                <div>
                  <span className="text-xs text-slate-400">Mean Package:</span>
                  <div className="text-2xl font-extrabold text-cyan-400">₹{comp.mean_package} LPA</div>
                </div>
                <div className="flex justify-between text-xs text-slate-400 border-t border-slate-800 pt-2">
                  <span>Median: <strong>₹{comp.median_package} LPA</strong></span>
                  <span>Share: <strong>{comp.share_pct}%</strong></span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Charts Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Company Type Bar Chart */}
        <div className="glass-panel detail-trigger p-6 rounded-2xl" role="button" tabIndex={0} onClick={() => onOpenDetail({ title: "Company package comparison", kicker: "Chart detail", description: "Mean placed-student compensation by company classification.", rows: company_stats.map((company) => ({ label: company.company_type, value: `₹${company.mean_package} LPA · ${company.count} placements` })) })}>
          <h2 className="text-lg font-bold text-white mb-1">Company Type Mean Package Comparison</h2>
          <p className="text-xs text-slate-400 mb-4">Average package compensation across company macro classifications</p>

          <div className="h-60 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={company_stats}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1E293B" />
                <XAxis dataKey="company_type" stroke="#94A3B8" fontSize={11} />
                <YAxis stroke="#64748B" fontSize={11} unit=" LPA" />
                <Tooltip contentStyle={{ backgroundColor: "#0F172A", borderColor: "#334155", borderRadius: "12px", color: "#F8FAFC" }} />
                <Bar dataKey="mean_package" name="Mean Package (LPA)" radius={[6, 6, 0, 0]}>
                  {company_stats.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={companyColors[entry.company_type] || "#3B82F6"} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Branch Mean Package Chart */}
        <div className="glass-panel detail-trigger p-6 rounded-2xl" role="button" tabIndex={0} onClick={() => onOpenDetail({ title: "Department package comparison", kicker: "Chart detail", description: "Mean placed-student compensation by department in the active scope.", rows: branch_stats.map((branch) => ({ label: branch.branch, value: `₹${branch.avg_package} LPA · ${branch.placed} placements` })) })}>
          <h2 className="text-lg font-bold text-white mb-1">Branch Average Package (Placed Cohort)</h2>
          <p className="text-xs text-slate-400 mb-4">Compensation outcome averages across engineering branches</p>

          <div className="h-60 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={branch_stats}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1E293B" />
                <XAxis dataKey="branch" stroke="#94A3B8" fontSize={11} />
                <YAxis stroke="#64748B" fontSize={11} unit=" LPA" />
                <Tooltip contentStyle={{ backgroundColor: "#0F172A", borderColor: "#334155", borderRadius: "12px", color: "#F8FAFC" }} />
                <Bar dataKey="avg_package" fill="#6366F1" radius={[6, 6, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {/* Governance & NULL Semantics Panel */}
      <div className="p-4 rounded-2xl bg-slate-900/90 border border-slate-800 flex items-start gap-3">
        <ShieldAlert className="w-5 h-5 text-amber-400 flex-shrink-0 mt-0.5" />
        <div className="text-xs space-y-1">
          <h3 className="font-bold text-white text-sm">Strict NULL Package Governance</h3>
          <p className="text-slate-400">
            Package calculations apply exclusively to placed students in the active filter scope. Unplaced students maintain NULL package records and are never converted to ₹0.00 LPA to avoid biasing statistical averages.
          </p>
        </div>
      </div>
    </div>
  );
};
