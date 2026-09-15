import React from "react";
import { FileText, CheckCircle2, ShieldCheck, AlertTriangle, BookOpen, ExternalLink } from "lucide-react";
import { MagicMarquee } from "../magicui/MagicMarquee";

export const ReportsIntelligence = ({ data, onOpenDetail }) => {
  const { insights } = data;

  return (
    <div className="space-y-6 animate-fadeIn">
      {/* Header */}
      <div>
        <h1 className="text-2xl md:text-3xl font-bold text-white flex items-center gap-3">
          <span className="p-2 rounded-xl bg-cyan-500/10 text-cyan-400 border border-cyan-500/30">04</span>
          Reports & Intelligence
        </h1>
        <p className="text-slate-400 text-sm mt-1">
          Validated analytical insights, institutional reporting storytelling, and methodological limits
        </p>
      </div>

      {/* Marquee Ticker of Headline Insights */}
      <div className="glass-panel p-4 rounded-2xl overflow-hidden border border-slate-800">
        <h2 className="text-xs font-bold uppercase tracking-wider text-cyan-400 mb-2">Headline Validated Findings</h2>
        <MagicMarquee pauseOnHover className="[--duration:30s]">
          {insights.map((ins, idx) => (
            <button key={idx} onClick={() => onOpenDetail({ title: ins.title, kicker: `${ins.category} insight`, description: ins.summary, rows: [{ label: "Evidence scope", value: ins.scope }, { label: "Insight type", value: ins.type }, { label: "Validation", value: "Validated" }] })} className="w-80 glass-card p-4 rounded-xl border border-slate-800 flex flex-col justify-between shrink-0 text-left">
              <div className="flex justify-between items-center mb-2">
                <span className="text-[10px] font-bold text-cyan-400 bg-cyan-500/10 px-2 py-0.5 rounded border border-cyan-500/30">
                  {ins.id} • {ins.category}
                </span>
                <span className="text-[10px] text-slate-500 font-semibold">{ins.type}</span>
              </div>
              <h3 className="text-xs font-bold text-white mb-1 line-clamp-1">{ins.title}</h3>
              <p className="text-[11px] text-slate-400 line-clamp-2">{ins.summary}</p>
            </button>
          ))}
        </MagicMarquee>
      </div>

      {/* Full Insights Grid */}
      <div>
        <h2 className="text-lg font-bold text-white mb-3 flex items-center gap-2">
          <FileText className="w-5 h-5 text-cyan-400" />
          Validated Strategic Insight Repository
        </h2>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {insights.map((ins, idx) => (
            <button key={idx} onClick={() => onOpenDetail({ title: ins.title, kicker: `${ins.category} insight`, description: ins.summary, rows: [{ label: "Evidence scope", value: ins.scope }, { label: "Insight type", value: ins.type }, { label: "Validation", value: "Validated" }] })} className="glass-card detail-trigger p-5 rounded-2xl space-y-3 border border-slate-800 hover:border-cyan-500/40 text-left">
              <div className="flex justify-between items-center">
                <span className="text-xs font-bold text-cyan-400 bg-cyan-500/10 px-2.5 py-1 rounded-lg border border-cyan-500/20">
                  {ins.id}
                </span>
                <span className="text-xs text-slate-400 font-medium">{ins.scope} Scope</span>
              </div>

              <h3 className="text-base font-bold text-white leading-snug">{ins.title}</h3>
              <p className="text-xs text-slate-400 leading-relaxed">{ins.summary}</p>

              <div className="pt-2 border-t border-slate-800 flex justify-between items-center text-xs">
                <span className="text-slate-500 font-medium">Category: <strong className="text-slate-300">{ins.category}</strong></span>
                <span className="text-emerald-400 font-semibold flex items-center gap-1">
                  <CheckCircle2 className="w-3.5 h-3.5" /> Validated
                </span>
              </div>
            </button>
          ))}
        </div>
      </div>

      {/* Methodology & Limitations Panels */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Panel 1: Governance & Methodology */}
        <div className="glass-panel p-6 rounded-2xl space-y-3 border border-slate-800">
          <div className="flex items-center gap-2 text-cyan-400 font-bold text-base">
            <BookOpen className="w-5 h-5" />
            Institutional Governance & Baseline
          </div>
          <p className="text-xs text-slate-400 leading-relaxed">
            All dashboard analytics strictly reconcile to the 1,500-student cross-validated baseline established in Phase 3. The Placement Readiness Index (PRI) evaluates 6 non-target preparation components without outcome leakage.
          </p>
          <div className="space-y-1.5 pt-2 text-xs text-slate-300">
            <div className="flex items-center gap-2">
              <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
              <span>Python EDA + PostgreSQL + Power BI + React cross-validation</span>
            </div>
            <div className="flex items-center gap-2">
              <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
              <span>Immutable dataset hash verification (MD5 verified)</span>
            </div>
          </div>
        </div>

        {/* Panel 2: Analytical Scope & Limits */}
        <div className="glass-panel p-6 rounded-2xl space-y-3 border border-slate-800">
          <div className="flex items-center gap-2 text-amber-400 font-bold text-base">
            <AlertTriangle className="w-5 h-5" />
            Analytical Boundaries & Limitations
          </div>
          <p className="text-xs text-slate-400 leading-relaxed">
            The dataset represents a single-cohort observational snapshot (1,500 students). Findings reflect observed placement associations rather than causal guarantees or automated hiring rankings.
          </p>
          <div className="space-y-1.5 pt-2 text-xs text-slate-300">
            <div className="flex items-center gap-2">
              <span className="w-1.5 h-1.5 rounded-full bg-amber-400" />
              <span>No candidate ranking lists or automated hiring claims</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="w-1.5 h-1.5 rounded-full bg-amber-400" />
              <span>No historical recruitment trend timelines beyond dataset scope</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
