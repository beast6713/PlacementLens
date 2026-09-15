import React, { useState } from "react";
import { LayoutDashboard, Users, Building2, FileText, RotateCcw, Filter, Database, Menu, Search, Bell, MoreHorizontal, CalendarDays, X, SlidersHorizontal } from "lucide-react";
import placementData from "./data/placementData.json";
import { DetailModal } from "./components/DetailModal";
import { CommandCenter } from "./components/pages/CommandCenter";
import { StudentAnalytics } from "./components/pages/StudentAnalytics";
import { CompanyIntelligence } from "./components/pages/CompanyIntelligence";
import { ReportsIntelligence } from "./components/pages/ReportsIntelligence";

export default function App() {
  const [activePage, setActivePage] = useState("P01");
  const [filters, setFilters] = useState({ branch: "", gender: "", placed: "" });
  const [detail, setDetail] = useState(null);

  const handleResetFilters = () => {
    setFilters({ branch: "", gender: "", placed: "" });
  };

  const navItems = [
    { id: "P01", label: "01 Command Center", icon: LayoutDashboard, component: CommandCenter },
    { id: "P02", label: "02 Student & Placement", icon: Users, component: StudentAnalytics },
    { id: "P03", label: "03 Company & Package", icon: Building2, component: CompanyIntelligence },
    { id: "P04", label: "04 Reports & Intelligence", icon: FileText, component: ReportsIntelligence },
  ];

  const activeNav = navItems.find((item) => item.id === activePage) || navItems[0];
  const ActiveComponent = activeNav.component;
  const scopeLabel = [filters.branch, filters.gender, filters.placed === "1" ? "Placed" : filters.placed === "0" ? "Unplaced" : ""].filter(Boolean).join(" · ") || "All students";
  const openPage = (item) => {
    setActivePage(item.id);
    setDetail({ title: item.label.replace(/^\d+\s/, ""), kicker: "Dashboard tab", description: "The full interactive view is now loaded behind this summary. Close this dialog to explore its cards, charts, and records.", rows: [{ label: "Current filter scope", value: scopeLabel }, { label: "Available interactions", value: "Cards, chart panels, bars, and records" }] });
  };

  return (
    <div className="light-dashboard min-h-screen text-slate-700 flex overflow-x-hidden">
      <aside className="icon-rail hidden md:flex">
        <button className="rail-menu" aria-label="Menu"><Menu size={23} /></button>
        <nav>{navItems.map((item) => { const Icon = item.icon; return <button key={item.id} aria-label={item.label} onClick={() => openPage(item)} className={activePage === item.id ? "rail-item active" : "rail-item"}><Icon size={19} /></button>; })}</nav>
      </aside>

      <aside className="profile-panel hidden lg:flex">
        <div className="profile-panel-head"><span>Profile view</span><X size={15} /></div>
        <div className="profile-user"><div className="profile-avatar">PL</div><div><strong>PlacementLens</strong><span>Campus intelligence</span></div><MoreHorizontal size={18} /></div>
        <div className="profile-stat"><span>ACTIVE SCOPE</span><strong>{scopeLabel}</strong></div>
        <div className="profile-stat"><span>STUDENT COHORT</span><strong>{placementData.students.length.toLocaleString()} learners</strong></div>
        <div className="profile-filter-card">
          <div className="filter-card-title"><SlidersHorizontal size={16} /> Global filters</div>
          <label>Department<select value={filters.branch} onChange={(e) => setFilters({ ...filters, branch: e.target.value })}><option value="">All departments</option><option value="CE">Civil engineering</option><option value="EEE">Electrical engineering</option><option value="IT">Information technology</option><option value="CSE">Computer science</option><option value="ECE">Electronics & communication</option><option value="ME">Mechanical engineering</option></select></label>
          <label>Gender<select value={filters.gender} onChange={(e) => setFilters({ ...filters, gender: e.target.value })}><option value="">All genders</option><option value="Female">Female</option><option value="Male">Male</option></select></label>
          <label>Placement status<select value={filters.placed} onChange={(e) => setFilters({ ...filters, placed: e.target.value })}><option value="">All outcomes</option><option value="1">Placed</option><option value="0">Unplaced</option></select></label>
          <button className="reset-link" onClick={handleResetFilters}><RotateCcw size={14} /> Reset filters</button>
        </div>
        <div className="profile-footer"><Database size={14} /> Verified analytical dataset</div>
      </aside>

      <main className="flex-1 min-w-0 dashboard-main">
        <header className="dashboard-header">
          <div className="md:hidden"><Menu size={22} /></div>
          <div><div className="header-eyebrow">PlacementLens / {activeNav.label.replace(/^\d+\s/, "")}</div><h1>Dashboard</h1></div>
          <div className="header-date"><CalendarDays size={15} /> Interactive cohort view</div>
          <div className="header-actions"><button className="header-action" onClick={() => setDetail({ title: "Current filter scope", kicker: "Dashboard controls", description: "Every KPI and chart updates from this shared selection.", rows: [{ label: "Department", value: filters.branch || "All departments" }, { label: "Gender", value: filters.gender || "All genders" }, { label: "Outcome", value: filters.placed === "1" ? "Placed" : filters.placed === "0" ? "Unplaced" : "All outcomes" }] })}><Filter size={15} /> Filters</button><button className="icon-button" aria-label="Search" onClick={() => setDetail({ title: "Explore the student directory", description: "Open Student & Placement to search the active cohort by student ID or department." })}><Search size={19} /></button><button className="icon-button" aria-label="Notifications" onClick={() => setDetail({ title: "Insight notifications", description: "No new data-quality alerts. All metrics are calculated from the current active filter scope." })}><Bell size={19} /></button></div>
        </header>

        <div className="mobile-filters lg:hidden"><Filter size={15} /><select value={filters.branch} onChange={(e) => setFilters({ ...filters, branch: e.target.value })}><option value="">All departments</option><option value="CE">Civil</option><option value="EEE">Electrical</option><option value="IT">IT</option><option value="CSE">CSE</option><option value="ECE">ECE</option><option value="ME">Mechanical</option></select><button onClick={handleResetFilters}><RotateCcw size={14} /> Reset</button></div>

           {/* Branch Slicer */}
        <div className="dashboard-canvas">
          <div className="page-tabs">{navItems.map((item) => <button key={item.id} onClick={() => openPage(item)} className={activePage === item.id ? "tab-button active" : "tab-button"}>{item.label.replace(/^\d+\s/, "")}</button>)}</div>
          <ActiveComponent data={placementData} filters={filters} setFilters={setFilters} onOpenDetail={setDetail} />
        </div>
      </main>
      <DetailModal detail={detail} onClose={() => setDetail(null)} />
    </div>
  );
}
