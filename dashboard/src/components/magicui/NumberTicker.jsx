import React, { useEffect, useState } from "react";
import { cn } from "../../lib/utils";

export const NumberTicker = ({
  value,
  direction = "up",
  delay = 0,
  className,
  decimalPlaces = 0,
  prefix = "",
  suffix = "",
}) => {
  const [displayValue, setDisplayValue] = useState(0);

  useEffect(() => {
    let startTimestamp = null;
    const duration = 1500; // ms
    const target = parseFloat(value) || 0;

    const step = (timestamp) => {
      if (!startTimestamp) startTimestamp = timestamp;
      const progress = Math.min((timestamp - startTimestamp) / duration, 1);
      
      // Easing out cubic
      const easedProgress = 1 - Math.pow(1 - progress, 3);
      const current = easedProgress * target;
      
      setDisplayValue(current);

      if (progress < 1) {
        window.requestAnimationFrame(step);
      }
    };

    const timer = setTimeout(() => {
      window.requestAnimationFrame(step);
    }, delay * 1000);

    return () => clearTimeout(timer);
  }, [value, delay]);

  return (
    <span className={cn("inline-block tabular-nums font-bold tracking-tight", className)}>
      {prefix}
      {displayValue.toFixed(decimalPlaces)}
      {suffix}
    </span>
  );
};
