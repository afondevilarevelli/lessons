import React from "react";
import Image from "next/image";

export default function AuthLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="h-screen w-screen flex">
      <Image
        src={"/images/astronaut.jpg"}
        alt={"astronaut"}
        width={250}
        height={250}
        className="hidden xl:block flex-1 w-full h-auto object-cover"
      />

      <div className="flex-1 flex items-center justify-center">
        <div className="card w-96 bg-base-100 shadow-xl">
          <div className="card-body items-center text-center">{children}</div>
        </div>
      </div>
    </div>
  );
}
