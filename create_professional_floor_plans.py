#!/usr/bin/env python3
"""
Create 2 professional architectural floor plans similar to the provided sample
"""
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def draw_grid(c, width, height, grid_size=0.25*inch):
    """Draw background grid"""
    c.setStrokeColor(colors.Color(0.9, 0.9, 0.9))
    c.setLineWidth(0.5)
    
    # Vertical lines
    x = 0
    while x <= width:
        c.line(x, 0, x, height)
        x += grid_size
    
    # Horizontal lines
    y = 0
    while y <= height:
        c.line(0, y, width, y)
        y += grid_size

def draw_thick_wall(c, x1, y1, x2, y2, thickness=6):
    """Draw wall with thickness"""
    c.setLineWidth(thickness)
    c.setStrokeColor(colors.black)
    c.setFillColor(colors.black)
    c.line(x1, y1, x2, y2)

def draw_dimension_line(c, x1, y1, x2, y2, text, offset=15):
    """Draw dimension line with text"""
    c.setStrokeColor(colors.blue)
    c.setLineWidth(0.5)
    
    # Draw line
    c.line(x1, y1, x2, y2)
    
    # Draw end marks
    if x1 == x2:  # Vertical
        c.line(x1-3, y1, x1+3, y1)
        c.line(x2-3, y2, x2+3, y2)
        mid_y = (y1 + y2) / 2
        c.setFont("Helvetica", 7)
        c.setFillColor(colors.blue)
        c.drawString(x1 + offset, mid_y - 3, text)
    else:  # Horizontal
        c.line(x1, y1-3, x1, y1+3)
        c.line(x2, y2-3, x2, y2+3)
        mid_x = (x1 + x2) / 2
        c.setFont("Helvetica", 7)
        c.setFillColor(colors.blue)
        c.drawCentredString(mid_x, y1 + offset, text)

def draw_door(c, x, y, width, orientation='right'):
    """Draw door symbol"""
    c.setLineWidth(1.5)
    c.setStrokeColor(colors.black)
    
    if orientation == 'right':
        c.arc(x, y-width, x+width, y, 0, 90)
    elif orientation == 'left':
        c.arc(x-width, y-width, x, y, 90, 180)
    elif orientation == 'up':
        c.arc(x, y, x+width, y+width, 270, 360)
    elif orientation == 'down':
        c.arc(x, y-width, x+width, y, 0, 90)

def draw_window(c, x, y, width, is_vertical=False):
    """Draw window symbol"""
    c.setLineWidth(2)
    c.setStrokeColor(colors.black)
    
    if is_vertical:
        # Vertical window
        c.line(x, y, x, y+width)
        c.line(x+3, y, x+3, y+width)
    else:
        # Horizontal window
        c.line(x, y, x+width, y)
        c.line(x, y+3, x+width, y+3)

def draw_annotation(c, x, y, text, color=colors.red, font_size=7):
    """Draw annotation text"""
    c.setFont("Helvetica", font_size)
    c.setFillColor(color)
    c.drawString(x, y, text)

def draw_arrow(c, x1, y1, x2, y2, color=colors.red):
    """Draw arrow from point 1 to point 2"""
    c.setStrokeColor(color)
    c.setLineWidth(1)
    c.line(x1, y1, x2, y2)
    
    # Arrow head (simple)
    c.setFillColor(color)
    c.circle(x2, y2, 2, fill=1, stroke=0)

def add_room_label(c, x, y, room_name, dimensions, font_size=9):
    """Add room label with dimensions"""
    c.setFont("Helvetica-Bold", font_size)
    c.setFillColor(colors.black)
    c.drawCentredString(x, y + 8, room_name)
    
    c.setFont("Helvetica", 7)
    c.setFillColor(colors.Color(0.3, 0.3, 0.3))
    c.drawCentredString(x, y - 2, dimensions)

def create_floor_plan_variant_1():
    """Create Professional Floor Plan - Variant 1: Luxury 3BR Single Story"""
    filename = "/app/professional_floor_plan_variant_1.pdf"
    c = canvas.Canvas(filename, pagesize=landscape(letter))
    width, height = landscape(letter)
    
    # Draw grid background
    draw_grid(c, width, height)
    
    # Title block
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(colors.black)
    c.drawString(50, height - 40, "FIRST FLOOR PLAN")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 58, "LUXURY 3-BEDROOM RESIDENCE")
    
    # Scale
    scale = 0.12 * inch  # 1 foot = 0.12 inch
    origin_x = 80
    origin_y = 120
    
    # Overall dimensions: 65' x 45'
    total_width = 65 * scale
    total_height = 45 * scale
    
    # EXTERIOR WALLS (6" thick)
    draw_thick_wall(c, origin_x, origin_y, origin_x + total_width, origin_y, 6)  # Bottom
    draw_thick_wall(c, origin_x + total_width, origin_y, origin_x + total_width, origin_y + total_height, 6)  # Right
    draw_thick_wall(c, origin_x + total_width, origin_y + total_height, origin_x, origin_y + total_height, 6)  # Top
    draw_thick_wall(c, origin_x, origin_y + total_height, origin_x, origin_y, 6)  # Left
    
    # INTERIOR WALLS (4-5" thick)
    # Vertical walls
    draw_thick_wall(c, origin_x + 25*scale, origin_y, origin_x + 25*scale, origin_y + 30*scale, 4)
    draw_thick_wall(c, origin_x + 40*scale, origin_y, origin_x + 40*scale, origin_y + 45*scale, 4)
    draw_thick_wall(c, origin_x + 50*scale, origin_y + 30*scale, origin_x + 50*scale, origin_y + 45*scale, 4)
    
    # Horizontal walls
    draw_thick_wall(c, origin_x, origin_y + 30*scale, origin_x + 40*scale, origin_y + 30*scale, 4)
    draw_thick_wall(c, origin_x + 25*scale, origin_y + 20*scale, origin_x + 40*scale, origin_y + 20*scale, 4)
    draw_thick_wall(c, origin_x + 40*scale, origin_y + 15*scale, origin_x + 65*scale, origin_y + 15*scale, 4)
    
    # ROOM LABELS
    add_room_label(c, origin_x + 12.5*scale, origin_y + 37.5*scale, "GREAT ROOM", "25'-0\" x 15'-0\"")
    add_room_label(c, origin_x + 12.5*scale, origin_y + 15*scale, "MASTER BEDROOM", "25'-0\" x 10'-0\"")
    add_room_label(c, origin_x + 32.5*scale, origin_y + 37.5*scale, "DINING ROOM", "15'-0\" x 15'-0\"")
    add_room_label(c, origin_x + 32.5*scale, origin_y + 25*scale, "KITCHEN", "15'-0\" x 10'-0\"")
    add_room_label(c, origin_x + 32.5*scale, origin_y + 10*scale, "PANTRY", "15'-0\" x 10'-0\"")
    add_room_label(c, origin_x + 45*scale, origin_y + 37.5*scale, "BEDROOM 2", "10'-0\" x 15'-0\"")
    add_room_label(c, origin_x + 57.5*scale, origin_y + 37.5*scale, "BEDROOM 3", "15'-0\" x 15'-0\"")
    add_room_label(c, origin_x + 52.5*scale, origin_y + 22.5*scale, "BATH 2", "25'-0\" x 15'-0\"")
    add_room_label(c, origin_x + 52.5*scale, origin_y + 7.5*scale, "2-CAR GARAGE", "25'-0\" x 15'-0\"")
    
    # DOORS
    draw_door(c, origin_x + 25*scale, origin_y + 30*scale, 3*scale, 'right')
    draw_door(c, origin_x + 15*scale, origin_y + 30*scale, 3*scale, 'right')
    draw_door(c, origin_x + 40*scale, origin_y + 30*scale, 3*scale, 'right')
    draw_door(c, origin_x + 40*scale, origin_y + 37.5*scale, 3*scale, 'right')
    
    # WINDOWS
    draw_window(c, origin_x + 5*scale, origin_y + 45*scale, 8*scale, False)
    draw_window(c, origin_x + 5*scale, origin_y, 8*scale, False)
    draw_window(c, origin_x + 65*scale, origin_y + 37.5*scale, 8*scale, True)
    draw_window(c, origin_x + 47*scale, origin_y + 45*scale, 6*scale, False)
    
    # DIMENSIONS (Exterior)
    draw_dimension_line(c, origin_x, origin_y - 20, origin_x + total_width, origin_y - 20, "65'-0\"", 5)
    draw_dimension_line(c, origin_x - 20, origin_y, origin_x - 20, origin_y + total_height, "45'-0\"", -35)
    
    # ANNOTATIONS
    draw_annotation(c, origin_x + 10*scale, origin_y + 40*scale, "10' CEILING", colors.red, 7)
    draw_annotation(c, origin_x + 10*scale, origin_y + 10*scale, "TRAY CEILING", colors.red, 7)
    draw_annotation(c, origin_x + 30*scale, origin_y + 35*scale, "CROWN MOLDING", colors.red, 7)
    draw_annotation(c, origin_x + 50*scale, origin_y + 20*scale, "TILE FLOOR", colors.red, 7)
    
    # SQUARE FOOTAGE TABLE
    table_x = width - 200
    table_y = height - 150
    
    c.setStrokeColor(colors.black)
    c.setLineWidth(1)
    c.rect(table_x, table_y, 180, 120)
    
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.black)
    c.drawString(table_x + 10, table_y + 105, "SQUARE FOOTAGE CALCULATIONS")
    
    c.setFont("Helvetica", 8)
    c.drawString(table_x + 10, table_y + 90, "HEATED SQ. FT.")
    c.drawString(table_x + 10, table_y + 75, "  FIRST FLOOR:")
    c.drawRightString(table_x + 165, table_y + 75, "2,850 SQ. FT.")
    c.drawString(table_x + 10, table_y + 62, "  TOTAL HEATED SQ. FT.:")
    c.setFont("Helvetica-Bold", 8)
    c.drawRightString(table_x + 165, table_y + 62, "2,850 SQ. FT.")
    
    c.setFont("Helvetica", 8)
    c.drawString(table_x + 10, table_y + 45, "UNHEATED SQ. FT.")
    c.drawString(table_x + 10, table_y + 30, "  GARAGE:")
    c.drawRightString(table_x + 165, table_y + 30, "375 SQ. FT.")
    c.drawString(table_x + 10, table_y + 17, "  TOTAL UNHEATED SQ. FT.:")
    c.setFont("Helvetica-Bold", 8)
    c.drawRightString(table_x + 165, table_y + 17, "375 SQ. FT.")
    
    # LEGEND
    c.setFont("Helvetica", 7)
    c.drawString(50, 50, "SCALE: 1/8\" = 1'-0\"")
    c.drawString(50, 40, "WALL THICKNESS: EXTERIOR 6\" | INTERIOR 5\"")
    c.drawString(50, 30, "CEILING HEIGHT: 9'-0\" (UNLESS NOTED)")
    
    c.save()
    print(f"Created: {filename}")

def create_floor_plan_variant_2():
    """Create Professional Floor Plan - Variant 2: Two-Story 4BR Home"""
    filename = "/app/professional_floor_plan_variant_2.pdf"
    c = canvas.Canvas(filename, pagesize=landscape(letter))
    width, height = landscape(letter)
    
    # Draw grid background
    draw_grid(c, width, height)
    
    # Title block
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(colors.black)
    c.drawString(50, height - 40, "FIRST FLOOR PLAN")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 58, "TWO-STORY 4-BEDROOM RESIDENCE")
    
    scale = 0.11 * inch
    
    # FIRST FLOOR
    origin_x = 70
    origin_y = 120
    floor_width = 55 * scale
    floor_height = 40 * scale
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(origin_x, origin_y + floor_height + 15, "FIRST FLOOR")
    
    # Exterior walls
    draw_thick_wall(c, origin_x, origin_y, origin_x + floor_width, origin_y, 6)
    draw_thick_wall(c, origin_x + floor_width, origin_y, origin_x + floor_width, origin_y + floor_height, 6)
    draw_thick_wall(c, origin_x + floor_width, origin_y + floor_height, origin_x, origin_y + floor_height, 6)
    draw_thick_wall(c, origin_x, origin_y + floor_height, origin_x, origin_y, 6)
    
    # Interior walls - First Floor
    draw_thick_wall(c, origin_x + 30*scale, origin_y, origin_x + 30*scale, origin_y + 40*scale, 4)
    draw_thick_wall(c, origin_x + 15*scale, origin_y, origin_x + 15*scale, origin_y + 20*scale, 4)
    draw_thick_wall(c, origin_x, origin_y + 20*scale, origin_x + 30*scale, origin_y + 20*scale, 4)
    draw_thick_wall(c, origin_x + 30*scale, origin_y + 25*scale, origin_x + 55*scale, origin_y + 25*scale, 4)
    draw_thick_wall(c, origin_x + 42*scale, origin_y + 25*scale, origin_x + 42*scale, origin_y + 40*scale, 4)
    
    # Room labels - First Floor
    add_room_label(c, origin_x + 7.5*scale, origin_y + 30*scale, "FOYER", "15'-0\" x 10'-0\"", 8)
    add_room_label(c, origin_x + 7.5*scale, origin_y + 10*scale, "STUDY", "15'-0\" x 20'-0\"", 8)
    add_room_label(c, origin_x + 22.5*scale, origin_y + 10*scale, "POWDER", "15'-0\" x 20'-0\"", 8)
    add_room_label(c, origin_x + 22.5*scale, origin_y + 32.5*scale, "DINING", "15'-0\" x 10'-0\"", 8)
    add_room_label(c, origin_x + 36*scale, origin_y + 32.5*scale, "KITCHEN", "12'-0\" x 15'-0\"", 8)
    add_room_label(c, origin_x + 48.5*scale, origin_y + 32.5*scale, "NOOK", "13'-0\" x 15'-0\"", 8)
    add_room_label(c, origin_x + 42*scale, origin_y + 12.5*scale, "GREAT ROOM", "25'-0\" x 25'-0\"", 9)
    
    # Stairs indication
    c.setStrokeColor(colors.black)
    c.setLineWidth(1)
    for i in range(10):
        y_pos = origin_y + 22*scale + i*1.5*scale
        c.line(origin_x + 15*scale, y_pos, origin_x + 24*scale, y_pos)
    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(origin_x + 19.5*scale, origin_y + 28*scale, "UP")
    
    # SECOND FLOOR
    origin_x2 = origin_x + floor_width + 50
    origin_y2 = origin_y
    
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.black)
    c.drawString(origin_x2, origin_y2 + floor_height + 15, "SECOND FLOOR")
    
    # Exterior walls - Second Floor
    draw_thick_wall(c, origin_x2, origin_y2, origin_x2 + floor_width, origin_y2, 6)
    draw_thick_wall(c, origin_x2 + floor_width, origin_y2, origin_x2 + floor_width, origin_y2 + floor_height, 6)
    draw_thick_wall(c, origin_x2 + floor_width, origin_y2 + floor_height, origin_x2, origin_y2 + floor_height, 6)
    draw_thick_wall(c, origin_x2, origin_y2 + floor_height, origin_x2, origin_y2, 6)
    
    # Interior walls - Second Floor
    draw_thick_wall(c, origin_x2 + 25*scale, origin_y2, origin_x2 + 25*scale, origin_y2 + 40*scale, 4)
    draw_thick_wall(c, origin_x2 + 40*scale, origin_y2, origin_x2 + 40*scale, origin_y2 + 40*scale, 4)
    draw_thick_wall(c, origin_x2, origin_y2 + 20*scale, origin_x2 + 55*scale, origin_y2 + 20*scale, 4)
    draw_thick_wall(c, origin_x2 + 15*scale, origin_y2 + 20*scale, origin_x2 + 15*scale, origin_y2 + 40*scale, 4)
    draw_thick_wall(c, origin_x2 + 47*scale, origin_y2 + 20*scale, origin_x2 + 47*scale, origin_y2 + 40*scale, 4)
    
    # Room labels - Second Floor
    add_room_label(c, origin_x2 + 12.5*scale, origin_y2 + 30*scale, "MASTER BR", "25'-0\" x 10'-0\"", 8)
    add_room_label(c, origin_x2 + 12.5*scale, origin_y2 + 10*scale, "MASTER BATH", "25'-0\" x 20'-0\"", 8)
    add_room_label(c, origin_x2 + 32.5*scale, origin_y2 + 30*scale, "BEDROOM 2", "15'-0\" x 10'-0\"", 8)
    add_room_label(c, origin_x2 + 43.5*scale, origin_y2 + 30*scale, "BR 3", "7'-0\" x 10'-0\"", 7)
    add_room_label(c, origin_x2 + 51*scale, origin_y2 + 30*scale, "BR 4", "8'-0\" x 10'-0\"", 7)
    add_room_label(c, origin_x2 + 32.5*scale, origin_y2 + 10*scale, "BATH 2", "15'-0\" x 20'-0\"", 8)
    add_room_label(c, origin_x2 + 47*scale, origin_y2 + 10*scale, "LAUNDRY", "15'-0\" x 20'-0\"", 8)
    
    # Stairs indication - Second Floor
    for i in range(10):
        y_pos = origin_y2 + 22*scale + i*1.5*scale
        c.line(origin_x2 + 3*scale, y_pos, origin_x2 + 12*scale, y_pos)
    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(origin_x2 + 7.5*scale, origin_y2 + 28*scale, "DOWN")
    
    # DIMENSIONS
    draw_dimension_line(c, origin_x, origin_y - 20, origin_x + floor_width, origin_y - 20, "55'-0\"", 5)
    draw_dimension_line(c, origin_x - 20, origin_y, origin_x - 20, origin_y + floor_height, "40'-0\"", -35)
    
    # ANNOTATIONS with arrows
    draw_arrow(c, origin_x + 10*scale, origin_y + 35*scale, origin_x + 5*scale, origin_y + 38*scale, colors.red)
    draw_annotation(c, origin_x + 11*scale, origin_y + 35*scale, "ENTRY", colors.red, 7)
    
    draw_arrow(c, origin_x + 45*scale, origin_y + 35*scale, origin_x + 42*scale, origin_y + 38*scale, colors.red)
    draw_annotation(c, origin_x + 46*scale, origin_y + 35*scale, "WINDOWS", colors.red, 7)
    
    draw_annotation(c, origin_x + 35*scale, origin_y + 30*scale, "9' CEILING", colors.red, 7)
    draw_annotation(c, origin_x2 + 10*scale, origin_y2 + 33*scale, "VAULTED CEILING", colors.red, 7)
    
    # SQUARE FOOTAGE TABLE
    table_x = width - 200
    table_y = height - 180
    
    c.setStrokeColor(colors.black)
    c.setFillColor(colors.black)
    c.setLineWidth(1)
    c.rect(table_x, table_y, 180, 150)
    
    c.setFont("Helvetica-Bold", 10)
    c.drawString(table_x + 10, table_y + 135, "SQUARE FOOTAGE CALCULATIONS")
    c.drawString(table_x + 10, table_y + 122, "TO OUTSIDE OF FRAMING")
    
    c.setFont("Helvetica", 8)
    c.drawString(table_x + 10, table_y + 105, "HEATED SQ. FT.")
    c.drawString(table_x + 10, table_y + 90, "  FIRST FLOOR:")
    c.drawRightString(table_x + 165, table_y + 90, "2,100 SQ. FT.")
    c.drawString(table_x + 10, table_y + 77, "  SECOND FLOOR:")
    c.drawRightString(table_x + 165, table_y + 77, "2,100 SQ. FT.")
    c.drawString(table_x + 10, table_y + 64, "  TOTAL HEATED SQ. FT.:")
    c.setFont("Helvetica-Bold", 8)
    c.drawRightString(table_x + 165, table_y + 64, "4,200 SQ. FT.")
    
    c.setFont("Helvetica", 8)
    c.drawString(table_x + 10, table_y + 47, "UNHEATED SQ. FT.")
    c.drawString(table_x + 10, table_y + 32, "  COVERED PORCH:")
    c.drawRightString(table_x + 165, table_y + 32, "180 SQ. FT.")
    c.drawString(table_x + 10, table_y + 19, "  TOTAL UNHEATED SQ. FT.:")
    c.setFont("Helvetica-Bold", 8)
    c.drawRightString(table_x + 165, table_y + 19, "180 SQ. FT.")
    
    # LEGEND
    c.setFont("Helvetica", 7)
    c.setFillColor(colors.black)
    c.drawString(50, 60, "SCALE: 1/8\" = 1'-0\"")
    c.drawString(50, 50, "WALL THICKNESS: EXTERIOR 6\" | INTERIOR 5\"")
    c.drawString(50, 40, "CEILING HEIGHT: 9'-0\" (UNLESS NOTED)")
    c.drawString(50, 30, "ALL DIMENSIONS TO BE VERIFIED ON SITE")
    
    c.save()
    print(f"Created: {filename}")

if __name__ == "__main__":
    print("Creating 2 Professional Architectural Floor Plans...")
    print("=" * 70)
    
    create_floor_plan_variant_1()
    create_floor_plan_variant_2()
    
    print("=" * 70)
    print("Both professional floor plans created successfully!")
    print("\nFiles created:")
    print("1. professional_floor_plan_variant_1.pdf - Luxury 3BR Single Story (2,850 sq ft)")
    print("2. professional_floor_plan_variant_2.pdf - Two-Story 4BR Home (4,200 sq ft)")
