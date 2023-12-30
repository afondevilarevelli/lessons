"use client";

import { usePathname } from "next/navigation";
import React from "react";

export default function Layout({ children }: any) {
  const pathname = usePathname();
  const shouldShowLayout =
    !pathname.startsWith("/auth") && !pathname.startsWith("/dashboard");

  if (!shouldShowLayout) return <>{children}</>;

  return <>Layout</>;
}
