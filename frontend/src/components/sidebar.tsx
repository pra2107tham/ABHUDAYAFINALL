"use client"

import Link from "next/link"
import { usePathname } from "next/navigation"
import { cn } from "@/lib/utils"
import { Home, Grid, FileText, MapPin, Layers, LayoutDashboard } from "lucide-react"

const sidebarItems = [
  { name: "Home", icon: Home, href: "/" },
  
  { name: "Documents", icon: FileText, href: "/documents" },
  { name: "Maharashtra", icon: MapPin, href: "/maharashtra" },
  { name: "Schemes", icon: Layers, href: "/schemess" },

]

export function Sidebar() {
  const pathname = usePathname()

  return (
    <aside className="fixed top-16 left-0 w-[250px] h-[calc(100vh-4rem)] bg-white border-r shadow-sm overflow-y-auto">
      <nav className="p-4 space-y-1">
        {sidebarItems.map((item) => (
          <Link key={item.name} href={item.href}>
            <div
              className={cn(
                "flex items-center gap-3 px-4 h-11 rounded-md transition-colors",
                pathname === item.href ? "bg-blue-600 text-white" : "text-gray-600 hover:bg-gray-100",
              )}
            >
              <item.icon className="h-5 w-5" />
              <span className="font-medium">{item.name}</span>
            </div>
          </Link>
        ))}
      </nav>
    </aside>
  )
}

