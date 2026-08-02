#!/usr/bin/env python3
"""
Hermes Advanced Recoil Control System v2.0
Professional Recoil Patterns & Compensation
"""

import json
import math

class RecoilEngine:
    def __init__(self):
        self.patterns = {}
        self._init_patterns()
    
    def _init_patterns(self):
        """Initialize advanced recoil patterns for all weapons"""
        
        self.patterns = {
            "M4": {
                "name": "M4A1",
                "type": "assault_rifle",
                "fire_rate": 750,
                "recoil_pattern": [
                    {"x": 0.0, "y": 0.3, "bullet": 1},
                    {"x": 0.1, "y": 0.5, "bullet": 2},
                    {"x": -0.1, "y": 0.4, "bullet": 3},
                    {"x": 0.05, "y": 0.6, "bullet": 4},
                    {"x": -0.05, "y": 0.5, "bullet": 5},
                    {"x": 0.15, "y": 0.7, "bullet": 6},
                    {"x": -0.15, "y": 0.6, "bullet": 7},
                    {"x": 0.0, "y": 0.8, "bullet": 8},
                    {"x": 0.1, "y": 0.7, "bullet": 9},
                    {"x": -0.1, "y": 0.9, "bullet": 10}
                ],
                "compensation": {
                    "vertical": 0.88,
                    "horizontal": 0.75,
                    "smoothing": 0.92,
                    "burst_compensation": 0.85,
                    "spray_compensation": 0.80
                },
                "attachments": {
                    "grip": "vertical_foregrip",
                    "barrel": "extended_barrel",
                    "muzzle": "compensator"
                }
            },
            
            "AK47": {
                "name": "AK-47",
                "type": "assault_rifle",
                "fire_rate": 600,
                "recoil_pattern": [
                    {"x": 0.0, "y": 0.5, "bullet": 1},
                    {"x": 0.2, "y": 0.8, "bullet": 2},
                    {"x": -0.2, "y": 0.7, "bullet": 3},
                    {"x": 0.3, "y": 1.0, "bullet": 4},
                    {"x": -0.3, "y": 0.9, "bullet": 5},
                    {"x": 0.25, "y": 1.2, "bullet": 6},
                    {"x": -0.25, "y": 1.1, "bullet": 7},
                    {"x": 0.35, "y": 1.3, "bullet": 8},
                    {"x": -0.35, "y": 1.2, "bullet": 9},
                    {"x": 0.3, "y": 1.4, "bullet": 10}
                ],
                "compensation": {
                    "vertical": 0.85,
                    "horizontal": 0.70,
                    "smoothing": 0.88,
                    "burst_compensation": 0.80,
                    "spray_compensation": 0.75
                }
            },
            
            "MP5": {
                "name": "MP5",
                "type": "smg",
                "fire_rate": 900,
                "recoil_pattern": [
                    {"x": 0.0, "y": 0.2, "bullet": 1},
                    {"x": 0.05, "y": 0.3, "bullet": 2},
                    {"x": -0.05, "y": 0.25, "bullet": 3},
                    {"x": 0.1, "y": 0.35, "bullet": 4},
                    {"x": -0.1, "y": 0.3, "bullet": 5},
                    {"x": 0.08, "y": 0.4, "bullet": 6},
                    {"x": -0.08, "y": 0.35, "bullet": 7},
                    {"x": 0.12, "y": 0.45, "bullet": 8},
                    {"x": -0.12, "y": 0.4, "bullet": 9},
                    {"x": 0.1, "y": 0.5, "bullet": 10}
                ],
                "compensation": {
                    "vertical": 0.92,
                    "horizontal": 0.85,
                    "smoothing": 0.95,
                    "burst_compensation": 0.90,
                    "spray_compensation": 0.88
                }
            },
            
            "AWM": {
                "name": "AWM",
                "type": "sniper",
                "fire_rate": 40,
                "recoil_pattern": [
                    {"x": 0.0, "y": 2.0, "bullet": 1}
                ],
                "compensation": {
                    "vertical": 0.15,
                    "horizontal": 0.10,
                    "smoothing": 0.98,
                    "quickscope_compensation": 0.20,
                    "hardscope_compensation": 0.10
                },
                "bullet_drop": {
                    "enabled": True,
                    "gravity": 9.8,
                    "velocity": 1350,
                    "compensation": 0.95
                }
            },
            
            "SPAS12": {
                "name": "SPAS-12",
                "type": "shotgun",
                "fire_rate": 120,
                "recoil_pattern": [
                    {"x": 0.0, "y": 1.5, "bullet": 1}
                ],
                "compensation": {
                    "vertical": 1.0,
                    "horizontal": 0.9,
                    "smoothing": 0.85,
                    "pellet_optimization": True
                },
                "pellet_spread": {
                    "center_mass": 0.7,
                    "max_spread": 0.3,
                    "optimal_range": 10
                }
            },
            
            "RPD": {
                "name": "RPD",
                "type": "lmg",
                "fire_rate": 650,
                "recoil_pattern": [
                    {"x": 0.0, "y": 0.4, "bullet": 1},
                    {"x": 0.15, "y": 0.6, "bullet": 2},
                    {"x": -0.15, "y": 0.5, "bullet": 3},
                    {"x": 0.2, "y": 0.8, "bullet": 4},
                    {"x": -0.2, "y": 0.7, "bullet": 5},
                    {"x": 0.25, "y": 1.0, "bullet": 6},
                    {"x": -0.25, "y": 0.9, "bullet": 7},
                    {"x": 0.3, "y": 1.2, "bullet": 8},
                    {"x": -0.3, "y": 1.1, "bullet": 9},
                    {"x": 0.28, "y": 1.3, "bullet": 10}
                ],
                "compensation": {
                    "vertical": 0.90,
                    "horizontal": 0.72,
                    "smoothing": 0.88,
                    "sustained_fire_bonus": 1.15,
                    "overheat_management": True
                }
            }
        }
    
    def get_pattern(self, weapon_name):
        """Get recoil pattern for a weapon"""
        return self.patterns.get(weapon_name, None)
    
    def calculate_compensation(self, weapon_name, bullet_count, distance):
        """Calculate compensation for a specific bullet"""
        pattern = self.get_pattern(weapon_name)
        if not pattern:
            return {"x": 0, "y": 0}
        
        # Find the closest bullet in pattern
        closest = min(pattern["recoil_pattern"], 
                     key=lambda p: abs(p["bullet"] - bullet_count))
        
        # Apply distance scaling
        distance_factor = max(0.5, 1.0 - (distance / 1000))
        
        return {
            "x": -closest["x"] * pattern["compensation"]["horizontal"] * distance_factor,
            "y": -closest["y"] * pattern["compensation"]["vertical"] * distance_factor
        }
    
    def export_all(self):
        """Export all patterns as JSON"""
        return json.dumps(self.patterns, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    engine = RecoilEngine()
    
    print("=== Hermes Advanced Recoil Control System v2.0 ===\n")
    
    for weapon, data in engine.patterns.items():
        print(f"🔫 {data['name']} ({data['type']})")
        print(f"   Fire Rate: {data['fire_rate']} RPM")
        print(f"   Pattern Bullets: {len(data['recoil_pattern'])}")
        print(f"   Compensation: V={data['compensation']['vertical']:.0%} H={data['compensation']['horizontal']:.0%}")
        print()
    
    # Test compensation
    print("=== Compensation Test (M4, bullet 5, 50m) ===")
    comp = engine.calculate_compensation("M4", 5, 50)
    print(f"   X: {comp['x']:.3f}")
    print(f"   Y: {comp['y']:.3f}")
    
    # Export
    with open("/data/workspace/hermes-configs/RecoilPatterns.json", "w") as f:
        f.write(engine.export_all())
    print("\n✅ Exported to RecoilPatterns.json")
