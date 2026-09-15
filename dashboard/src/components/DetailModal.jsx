import React, { useEffect } from "react";
import { X, ArrowUpRight } from "lucide-react";

export const DetailModal = ({ detail, onClose }) => {
  useEffect(() => {
    const closeOnEscape = (event) => event.key === "Escape" && onClose();
    window.addEventListener("keydown", closeOnEscape);
    return () => window.removeEventListener("keydown", closeOnEscape);
  }, [onClose]);

  if (!detail) return null;

  return (
    <div className="detail-overlay" role="presentation" onMouseDown={onClose}>
      <section className="detail-modal" role="dialog" aria-modal="true" aria-labelledby="detail-title" onMouseDown={(event) => event.stopPropagation()}>
        <button className="detail-close" onClick={onClose} aria-label="Close details"><X size={19} /></button>
        <div className="detail-kicker">{detail.kicker || "PlacementLens detail"}</div>
        <h2 id="detail-title">{detail.title}</h2>
        {detail.description && <p className="detail-description">{detail.description}</p>}
        {detail.rows?.length > 0 && (
          <div className="detail-rows">
            {detail.rows.map((row) => (
              <div className="detail-row" key={row.label}>
                <span>{row.label}</span>
                <strong>{row.value}</strong>
              </div>
            ))}
          </div>
        )}
        {detail.note && <p className="detail-note"><ArrowUpRight size={15} />{detail.note}</p>}
      </section>
    </div>
  );
};
