import React from "react";
import { cn } from "../../lib/utils";

export const ShimmerButton = React.forwardRef(
  (
    {
      shimmerColor = "#00F0FF",
      shimmerSize = "0.1em",
      shimmerDuration = "2.5s",
      borderRadius = "100px",
      background = "rgba(15, 23, 42, 1)",
      className,
      children,
      ...props
    },
    ref
  ) => {
    return (
      <button
        style={{
          "--spread": "90deg",
          "--shimmer-color": shimmerColor,
          "--radius": borderRadius,
          "--speed": shimmerDuration,
          "--cut": shimmerSize,
          "--bg": background,
        }}
        className={cn(
          "group relative z-0 flex cursor-pointer items-center justify-center overflow-hidden whitespace-nowrap border border-slate-700 px-4 py-2 font-medium text-slate-200 shadow-md transition-all duration-300 hover:border-cyan-400 hover:text-white hover:shadow-cyan-500/20 active:scale-95 [border-radius:var(--radius)]",
          className
        )}
        ref={ref}
        {...props}
      >
        <span className="z-10 flex items-center gap-2">{children}</span>

        {/* Highlight glow */}
        <div className="absolute inset-0 z-0 bg-gradient-to-r from-transparent via-cyan-500/10 to-transparent opacity-0 transition-opacity duration-300 group-hover:opacity-100" />
      </button>
    );
  }
);

ShimmerButton.displayName = "ShimmerButton";
