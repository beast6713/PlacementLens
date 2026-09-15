import React from "react";
import { cn } from "../../lib/utils";

export const BentoGrid = ({ className, children }) => {
  return (
    <div
      className={cn(
        "grid w-full auto-rows-[22rem] grid-cols-1 md:grid-cols-3 gap-4",
        className
      )}
    >
      {children}
    </div>
  );
};

export const BentoCard = ({
  name,
  className,
  background,
  Icon,
  description,
  href,
  cta,
  onClick,
  children,
}) => {
  return (
    <div
      className={cn(
        "group relative col-span-1 flex flex-col justify-between overflow-hidden rounded-2xl glass-card p-6 border border-slate-800/80 transition-all duration-300 hover:border-cyan-500/40 hover:shadow-lg hover:shadow-cyan-500/10",
        className
      )}
      onClick={onClick}
      role={onClick ? "button" : undefined}
      tabIndex={onClick ? 0 : undefined}
      onKeyDown={(event) => onClick && event.key === "Enter" && onClick()}
    >
      <div>{background}</div>
      <div className="pointer-events-none z-10 flex transform-gpu flex-col gap-1 transition-all duration-300 group-hover:-translate-y-1">
        {Icon && (
          <Icon className="h-8 w-8 origin-left transform-gpu text-cyan-400 transition-all duration-300 ease-in-out group-hover:scale-110 mb-2" />
        )}
        <h3 className="text-xl font-bold tracking-tight text-white">
          {name}
        </h3>
        {description && (
          <p className="max-w-lg text-sm text-slate-400 font-normal">
            {description}
          </p>
        )}
      </div>

      <div className="relative z-10 mt-4 flex-1">
        {children}
      </div>
    </div>
  );
};
