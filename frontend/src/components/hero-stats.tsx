"use client"

import { motion } from "framer-motion"

const stats = [
  {
    number: "207",
    label: "Government Department Integrations",
    bgColor: "bg-[#F0FFF0]",
    textColor: "text-[#2E7D32]",
    icon: "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-XVv0ZfVZ1op5lLI1eXtSWSNiBz1KlJ.png",
  },
  {
    number: "537.75 Cr",
    label: "Digital Tracking, Hassle-Free Governance",
    bgColor: "bg-[#E3F2FD]",
    textColor: "text-[#1976D2]",
    icon: "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-XVv0ZfVZ1op5lLI1eXtSWSNiBz1KlJ.png",
  },
  {
    number: "23",
    label: "Official and Regional Languages",
    bgColor: "bg-[#FFF0F7]",
    textColor: "text-[#E91E63]",
    icon: "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-XVv0ZfVZ1op5lLI1eXtSWSNiBz1KlJ.png",
  },
]

export function HeroStats() {
  return (
    <div className="w-full max-w-[1600px] mx-auto mb-12">
      <div className="mb-8">
        <h1 className="text-4xl font-bold text-gray-900 mb-2">Welcome to UMANG</h1>
        <p className="text-gray-600 text-lg">Unified Mobile Application for New-age Governance</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {stats.map((stat, index) => (
          <motion.div
            key={index}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.2 }}
            className={`${stat.bgColor} rounded-2xl p-8 transition-shadow duration-200`}
          >
            <div className="flex flex-col h-full">
              <div className="flex items-start justify-between mb-6">
                <div className="relative w-32 h-32">
                  {index === 0 && (
                    <div className="w-full h-full grid grid-cols-2 grid-rows-2 gap-2">
                      <div className="bg-[#B0BEC5] rounded-lg"></div>
                      <div className="bg-[#90A4AE] rounded-lg"></div>
                      <div className="bg-[#78909C] rounded-lg"></div>
                      <div className="bg-[#607D8B] rounded-lg"></div>
                    </div>
                  )}
                  {index === 1 && (
                    <div className="w-full h-full relative">
                      <div className="absolute inset-0">
                        <svg viewBox="0 0 100 100" className="w-full h-full">
                          <circle cx="50" cy="50" r="40" fill="#E3F2FD" />
                          <path d="M50,10 A40,40 0 0,1 90,50" stroke="#2196F3" strokeWidth="8" fill="none" />
                          <path d="M90,50 A40,40 0 0,1 50,90" stroke="#F44336" strokeWidth="8" fill="none" />
                          <path d="M50,90 A40,40 0 0,1 10,50" stroke="#4CAF50" strokeWidth="8" fill="none" />
                        </svg>
                        <div className="absolute right-0 bottom-0 flex gap-1">
                          <div className="w-3 h-12 bg-[#2196F3] rounded-t-lg"></div>
                          <div className="w-3 h-16 bg-[#F44336] rounded-t-lg"></div>
                          <div className="w-3 h-8 bg-[#4CAF50] rounded-t-lg"></div>
                        </div>
                      </div>
                    </div>
                  )}
                  {index === 2 && (
                    <div className="w-full h-full relative">
                      <div className="absolute inset-0 flex flex-wrap gap-2 justify-center items-center">
                        {["हिंदी", "বাংলা", "తెలుగు", "മലയാളം"].map((lang, i) => (
                          <div
                            key={i}
                            className="px-2 py-1 rounded-full text-xs"
                            style={{
                              backgroundColor: ["#FF8A80", "#82B1FF", "#B9F6CA", "#FFD180"][i],
                              transform: `rotate(${Math.random() * 20 - 10}deg)`,
                            }}
                          >
                            {lang}
                          </div>
                        ))}
                      </div>
                    </div>
                  )}
                </div>
                <motion.div
                  initial={{ scale: 0.5 }}
                  animate={{ scale: 1 }}
                  className={`text-4xl font-bold ${stat.textColor}`}
                >
                  {stat.number}
                </motion.div>
              </div>
              <p className="text-gray-600 text-lg">{stat.label}</p>
            </div>
          </motion.div>
        ))}
      </div>
    </div>
  )
}

