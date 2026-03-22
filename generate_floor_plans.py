#!/usr/bin/env python3
"""
Generate 5 sample US residential floor plan PDFs for drywall estimation testing
"""
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def draw_wall(c, x1, y1, x2, y2, thickness=4):
    """Draw a wall with given thickness"""
    c.setLineWidth(thickness)
    c.setStrokeColor(colors.black)
    c.line(x1, y1, x2, y2)

def draw_door(c, x, y, width, is_vertical=False):
    """Draw a door opening"""
    c.setLineWidth(1)
    c.setStrokeColor(colors.grey)
    if is_vertical:
        c.arc(x-width, y, x, y+width, 0, 90)
    else:
        c.arc(x, y, x+width, y+width, 0, 90)

def draw_window(c, x, y, width, is_vertical=False):
    """Draw a window"""
    c.setLineWidth(2)
    c.setStrokeColor(colors.black)
    if is_vertical:
        c.rect(x-2, y, 4, width, stroke=1, fill=0)
    else:
        c.rect(x, y-2, width, 4, stroke=1, fill=0)

def add_dimension(c, x, y, text, size=8):
    """Add dimension text"""
    c.setFont("Helvetica", size)
    c.setFillColor(colors.blue)
    c.drawString(x, y, text)

def add_room_label(c, x, y, text, size=10):
    """Add room label"""
    c.setFont("Helvetica-Bold", size)
    c.setFillColor(colors.black)
    c.drawCentredString(x, y, text)

# Floor Plan 1: Single-Story 3BR Ranch (1,800 sq ft)
def create_single_story_3br():
    filename = "/app/floor_plan_1_single_story_3br.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Floor Plan 1: Single-Story 3BR Ranch House")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 70, "Total Area: 1,800 sq ft | Ceiling Height: 9 ft")
    
    # Scale: 1 inch = 10 feet
    scale = 0.1 * inch  # 10 feet = 1 inch
    origin_x = 100
    origin_y = 150
    
    # Exterior walls (60' x 30')
    draw_wall(c, origin_x, origin_y, origin_x + 60*scale, origin_y, 6)  # Bottom
    draw_wall(c, origin_x + 60*scale, origin_y, origin_x + 60*scale, origin_y + 30*scale, 6)  # Right
    draw_wall(c, origin_x + 60*scale, origin_y + 30*scale, origin_x, origin_y + 30*scale, 6)  # Top
    draw_wall(c, origin_x, origin_y + 30*scale, origin_x, origin_y, 6)  # Left
    
    # Interior walls
    # Vertical walls
    draw_wall(c, origin_x + 20*scale, origin_y, origin_x + 20*scale, origin_y + 30*scale, 4)
    draw_wall(c, origin_x + 40*scale, origin_y, origin_x + 40*scale, origin_y + 20*scale, 4)
    
    # Horizontal walls
    draw_wall(c, origin_x, origin_y + 20*scale, origin_x + 20*scale, origin_y + 20*scale, 4)
    draw_wall(c, origin_x + 40*scale, origin_y + 20*scale, origin_x + 60*scale, origin_y + 20*scale, 4)
    draw_wall(c, origin_x + 20*scale, origin_y + 15*scale, origin_x + 40*scale, origin_y + 15*scale, 4)
    
    # Room labels and dimensions
    add_room_label(c, origin_x + 10*scale, origin_y + 25*scale, "Master Bedroom")
    add_dimension(c, origin_x + 5*scale, origin_y + 22*scale, "20' x 10'", 7)
    
    add_room_label(c, origin_x + 10*scale, origin_y + 10*scale, "Bedroom 2")
    add_dimension(c, origin_x + 5*scale, origin_y + 7*scale, "20' x 20'", 7)
    
    add_room_label(c, origin_x + 30*scale, origin_y + 25*scale, "Living Room")
    add_dimension(c, origin_x + 25*scale, origin_y + 22*scale, "20' x 10'", 7)
    
    add_room_label(c, origin_x + 30*scale, origin_y + 7*scale, "Kitchen")
    add_dimension(c, origin_x + 27*scale, origin_y + 4*scale, "20' x 15'", 7)
    
    add_room_label(c, origin_x + 50*scale, origin_y + 25*scale, "Bedroom 3")
    add_dimension(c, origin_x + 45*scale, origin_y + 22*scale, "20' x 10'", 7)
    
    add_room_label(c, origin_x + 50*scale, origin_y + 10*scale, "Bathroom")
    add_dimension(c, origin_x + 47*scale, origin_y + 7*scale, "20' x 20'", 7)
    
    # Doors
    draw_door(c, origin_x + 10*scale, origin_y + 20*scale, 3*scale, False)
    draw_door(c, origin_x + 10*scale, origin_y, 3*scale, False)
    draw_door(c, origin_x + 30*scale, origin_y + 15*scale, 3*scale, False)
    
    # Windows
    draw_window(c, origin_x, origin_y + 25*scale, 4*scale, True)
    draw_window(c, origin_x + 30*scale, origin_y + 30*scale, 8*scale, False)
    draw_window(c, origin_x + 60*scale, origin_y + 25*scale, 4*scale, True)
    
    # Dimensions
    add_dimension(c, origin_x + 25*scale, origin_y - 15, "60'-0\"", 9)
    add_dimension(c, origin_x - 30, origin_y + 15*scale, "30'-0\"", 9)
    
    c.save()
    print(f"Created: {filename}")

# Floor Plan 2: Single-Story 2BR Bungalow (1,200 sq ft)
def create_single_story_2br():
    filename = "/app/floor_plan_2_single_story_2br.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Floor Plan 2: Single-Story 2BR Bungalow")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 70, "Total Area: 1,200 sq ft | Ceiling Height: 8 ft")
    
    scale = 0.1 * inch
    origin_x = 100
    origin_y = 150
    
    # Exterior walls (40' x 30')
    draw_wall(c, origin_x, origin_y, origin_x + 40*scale, origin_y, 6)
    draw_wall(c, origin_x + 40*scale, origin_y, origin_x + 40*scale, origin_y + 30*scale, 6)
    draw_wall(c, origin_x + 40*scale, origin_y + 30*scale, origin_x, origin_y + 30*scale, 6)
    draw_wall(c, origin_x, origin_y + 30*scale, origin_x, origin_y, 6)
    
    # Interior walls
    draw_wall(c, origin_x + 15*scale, origin_y, origin_x + 15*scale, origin_y + 30*scale, 4)
    draw_wall(c, origin_x + 30*scale, origin_y, origin_x + 30*scale, origin_y + 18*scale, 4)
    draw_wall(c, origin_x, origin_y + 18*scale, origin_x + 15*scale, origin_y + 18*scale, 4)
    draw_wall(c, origin_x + 30*scale, origin_y + 18*scale, origin_x + 40*scale, origin_y + 18*scale, 4)
    
    # Room labels
    add_room_label(c, origin_x + 7.5*scale, origin_y + 24*scale, "Master BR")
    add_dimension(c, origin_x + 3*scale, origin_y + 21*scale, "15' x 12'", 7)
    
    add_room_label(c, origin_x + 7.5*scale, origin_y + 9*scale, "Bedroom 2")
    add_dimension(c, origin_x + 3*scale, origin_y + 6*scale, "15' x 18'", 7)
    
    add_room_label(c, origin_x + 22.5*scale, origin_y + 24*scale, "Living/Dining")
    add_dimension(c, origin_x + 18*scale, origin_y + 21*scale, "15' x 12'", 7)
    
    add_room_label(c, origin_x + 22.5*scale, origin_y + 9*scale, "Kitchen")
    add_dimension(c, origin_x + 19*scale, origin_y + 6*scale, "15' x 18'", 7)
    
    add_room_label(c, origin_x + 35*scale, origin_y + 24*scale, "Bath 1")
    add_dimension(c, origin_x + 32*scale, origin_y + 21*scale, "10' x 12'", 7)
    
    add_room_label(c, origin_x + 35*scale, origin_y + 9*scale, "Bath 2")
    add_dimension(c, origin_x + 32*scale, origin_y + 6*scale, "10' x 18'", 7)
    
    # Dimensions
    add_dimension(c, origin_x + 15*scale, origin_y - 15, "40'-0\"", 9)
    add_dimension(c, origin_x - 30, origin_y + 15*scale, "30'-0\"", 9)
    
    c.save()
    print(f"Created: {filename}")

# Floor Plan 3: Two-Story 4BR Colonial (2,400 sq ft)
def create_two_story_4br():
    filename = "/app/floor_plan_3_two_story_4br.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Floor Plan 3: Two-Story 4BR Colonial")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 70, "First Floor: 1,200 sq ft | Second Floor: 1,200 sq ft | Ceiling: 9 ft each floor")
    
    scale = 0.08 * inch
    
    # FIRST FLOOR
    origin_x = 80
    origin_y = 350
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(origin_x, origin_y + 35*scale, "FIRST FLOOR")
    
    # Exterior (40' x 30')
    draw_wall(c, origin_x, origin_y, origin_x + 40*scale, origin_y, 6)
    draw_wall(c, origin_x + 40*scale, origin_y, origin_x + 40*scale, origin_y + 30*scale, 6)
    draw_wall(c, origin_x + 40*scale, origin_y + 30*scale, origin_x, origin_y + 30*scale, 6)
    draw_wall(c, origin_x, origin_y + 30*scale, origin_x, origin_y, 6)
    
    # Interior walls
    draw_wall(c, origin_x + 25*scale, origin_y, origin_x + 25*scale, origin_y + 30*scale, 4)
    draw_wall(c, origin_x, origin_y + 15*scale, origin_x + 25*scale, origin_y + 15*scale, 4)
    
    add_room_label(c, origin_x + 12.5*scale, origin_y + 22.5*scale, "Living Room")
    add_dimension(c, origin_x + 8*scale, origin_y + 20*scale, "25' x 15'", 7)
    
    add_room_label(c, origin_x + 12.5*scale, origin_y + 7.5*scale, "Kitchen/Dining")
    add_dimension(c, origin_x + 7*scale, origin_y + 5*scale, "25' x 15'", 7)
    
    add_room_label(c, origin_x + 32.5*scale, origin_y + 15*scale, "Garage")
    add_dimension(c, origin_x + 29*scale, origin_y + 12*scale, "15' x 30'", 7)
    
    add_dimension(c, origin_x + 15*scale, origin_y - 12, "40'-0\"", 8)
    add_dimension(c, origin_x - 25, origin_y + 15*scale, "30'-0\"", 8)
    
    # SECOND FLOOR
    origin_x2 = 380
    origin_y2 = 350
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(origin_x2, origin_y2 + 35*scale, "SECOND FLOOR")
    
    # Exterior
    draw_wall(c, origin_x2, origin_y2, origin_x2 + 40*scale, origin_y2, 6)
    draw_wall(c, origin_x2 + 40*scale, origin_y2, origin_x2 + 40*scale, origin_y2 + 30*scale, 6)
    draw_wall(c, origin_x2 + 40*scale, origin_y2 + 30*scale, origin_x2, origin_y2 + 30*scale, 6)
    draw_wall(c, origin_x2, origin_y2 + 30*scale, origin_x2, origin_y2, 6)
    
    # Interior walls
    draw_wall(c, origin_x2 + 20*scale, origin_y2, origin_x2 + 20*scale, origin_y2 + 30*scale, 4)
    draw_wall(c, origin_x2, origin_y2 + 15*scale, origin_x2 + 40*scale, origin_y2 + 15*scale, 4)
    draw_wall(c, origin_x2 + 30*scale, origin_y2 + 15*scale, origin_x2 + 30*scale, origin_y2 + 30*scale, 4)
    
    add_room_label(c, origin_x2 + 10*scale, origin_y2 + 22.5*scale, "Master BR")
    add_dimension(c, origin_x2 + 5*scale, origin_y2 + 20*scale, "20' x 15'", 7)
    
    add_room_label(c, origin_x2 + 10*scale, origin_y2 + 7.5*scale, "Bedroom 2")
    add_dimension(c, origin_x2 + 5*scale, origin_y2 + 5*scale, "20' x 15'", 7)
    
    add_room_label(c, origin_x2 + 25*scale, origin_y2 + 22.5*scale, "BR 3")
    add_dimension(c, origin_x2 + 22*scale, origin_y2 + 20*scale, "10' x 15'", 7)
    
    add_room_label(c, origin_x2 + 35*scale, origin_y2 + 22.5*scale, "BR 4")
    add_dimension(c, origin_x2 + 32*scale, origin_y2 + 20*scale, "10' x 15'", 7)
    
    add_room_label(c, origin_x2 + 25*scale, origin_y2 + 7.5*scale, "Bath")
    add_dimension(c, origin_x2 + 22*scale, origin_y2 + 5*scale, "20' x 15'", 7)
    
    add_dimension(c, origin_x2 + 15*scale, origin_y2 - 12, "40'-0\"", 8)
    add_dimension(c, origin_x2 - 25, origin_y2 + 15*scale, "30'-0\"", 8)
    
    c.save()
    print(f"Created: {filename}")

# Floor Plan 4: Two-Story 3BR (2,000 sq ft)
def create_two_story_3br():
    filename = "/app/floor_plan_4_two_story_3br.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Floor Plan 4: Two-Story 3BR Home")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 70, "First Floor: 1,000 sq ft | Second Floor: 1,000 sq ft | Ceiling: 8 ft each")
    
    scale = 0.09 * inch
    
    # FIRST FLOOR
    origin_x = 80
    origin_y = 340
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(origin_x, origin_y + 32*scale, "FIRST FLOOR")
    
    # Exterior (40' x 25')
    draw_wall(c, origin_x, origin_y, origin_x + 40*scale, origin_y, 6)
    draw_wall(c, origin_x + 40*scale, origin_y, origin_x + 40*scale, origin_y + 25*scale, 6)
    draw_wall(c, origin_x + 40*scale, origin_y + 25*scale, origin_x, origin_y + 25*scale, 6)
    draw_wall(c, origin_x, origin_y + 25*scale, origin_x, origin_y, 6)
    
    draw_wall(c, origin_x + 20*scale, origin_y, origin_x + 20*scale, origin_y + 25*scale, 4)
    draw_wall(c, origin_x + 20*scale, origin_y + 12*scale, origin_x + 40*scale, origin_y + 12*scale, 4)
    
    add_room_label(c, origin_x + 10*scale, origin_y + 12.5*scale, "Living/Dining")
    add_dimension(c, origin_x + 6*scale, origin_y + 10*scale, "20' x 25'", 7)
    
    add_room_label(c, origin_x + 30*scale, origin_y + 18.5*scale, "Kitchen")
    add_dimension(c, origin_x + 27*scale, origin_y + 16*scale, "20' x 13'", 7)
    
    add_room_label(c, origin_x + 30*scale, origin_y + 6*scale, "Half Bath")
    add_dimension(c, origin_x + 27*scale, origin_y + 4*scale, "20' x 12'", 7)
    
    add_dimension(c, origin_x + 15*scale, origin_y - 12, "40'-0\"", 8)
    add_dimension(c, origin_x - 25, origin_y + 12.5*scale, "25'-0\"", 8)
    
    # SECOND FLOOR
    origin_x2 = 380
    origin_y2 = 340
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(origin_x2, origin_y2 + 32*scale, "SECOND FLOOR")
    
    draw_wall(c, origin_x2, origin_y2, origin_x2 + 40*scale, origin_y2, 6)
    draw_wall(c, origin_x2 + 40*scale, origin_y2, origin_x2 + 40*scale, origin_y2 + 25*scale, 6)
    draw_wall(c, origin_x2 + 40*scale, origin_y2 + 25*scale, origin_x2, origin_y2 + 25*scale, 6)
    draw_wall(c, origin_x2, origin_y2 + 25*scale, origin_x2, origin_y2, 6)
    
    draw_wall(c, origin_x2 + 15*scale, origin_y2, origin_x2 + 15*scale, origin_y2 + 25*scale, 4)
    draw_wall(c, origin_x2 + 25*scale, origin_y2, origin_x2 + 25*scale, origin_y2 + 25*scale, 4)
    
    add_room_label(c, origin_x2 + 7.5*scale, origin_y2 + 12.5*scale, "Master BR")
    add_dimension(c, origin_x2 + 4*scale, origin_y2 + 10*scale, "15' x 25'", 7)
    
    add_room_label(c, origin_x2 + 20*scale, origin_y2 + 12.5*scale, "BR 2")
    add_dimension(c, origin_x2 + 17*scale, origin_y2 + 10*scale, "10' x 25'", 7)
    
    add_room_label(c, origin_x2 + 32.5*scale, origin_y2 + 12.5*scale, "BR 3 + Bath")
    add_dimension(c, origin_x2 + 28*scale, origin_y2 + 10*scale, "15' x 25'", 7)
    
    add_dimension(c, origin_x2 + 15*scale, origin_y2 - 12, "40'-0\"", 8)
    add_dimension(c, origin_x2 - 25, origin_y2 + 12.5*scale, "25'-0\"", 8)
    
    c.save()
    print(f"Created: {filename}")

# Floor Plan 5: 1BR Apartment (800 sq ft)
def create_apartment_1br():
    filename = "/app/floor_plan_5_apartment_1br.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Floor Plan 5: 1BR Apartment")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 70, "Total Area: 800 sq ft | Ceiling Height: 8 ft")
    
    scale = 0.12 * inch
    origin_x = 150
    origin_y = 200
    
    # Exterior (32' x 25')
    draw_wall(c, origin_x, origin_y, origin_x + 32*scale, origin_y, 6)
    draw_wall(c, origin_x + 32*scale, origin_y, origin_x + 32*scale, origin_y + 25*scale, 6)
    draw_wall(c, origin_x + 32*scale, origin_y + 25*scale, origin_x, origin_y + 25*scale, 6)
    draw_wall(c, origin_x, origin_y + 25*scale, origin_x, origin_y, 6)
    
    # Interior walls
    draw_wall(c, origin_x + 20*scale, origin_y, origin_x + 20*scale, origin_y + 15*scale, 4)
    draw_wall(c, origin_x, origin_y + 15*scale, origin_x + 32*scale, origin_y + 15*scale, 4)
    draw_wall(c, origin_x + 12*scale, origin_y + 15*scale, origin_x + 12*scale, origin_y + 25*scale, 4)
    
    # Room labels
    add_room_label(c, origin_x + 10*scale, origin_y + 7.5*scale, "Bedroom")
    add_dimension(c, origin_x + 6*scale, origin_y + 5*scale, "20' x 15'", 8)
    
    add_room_label(c, origin_x + 26*scale, origin_y + 7.5*scale, "Bathroom")
    add_dimension(c, origin_x + 23*scale, origin_y + 5*scale, "12' x 15'", 8)
    
    add_room_label(c, origin_x + 6*scale, origin_y + 20*scale, "Kitchen")
    add_dimension(c, origin_x + 4*scale, origin_y + 18*scale, "12' x 10'", 8)
    
    add_room_label(c, origin_x + 22*scale, origin_y + 20*scale, "Living/Dining")
    add_dimension(c, origin_x + 17*scale, origin_y + 18*scale, "20' x 10'", 8)
    
    # Doors
    draw_door(c, origin_x + 8*scale, origin_y + 15*scale, 2.5*scale, False)
    draw_door(c, origin_x + 20*scale, origin_y + 7.5*scale, 2.5*scale, True)
    
    # Windows
    draw_window(c, origin_x + 5*scale, origin_y, 6*scale, False)
    draw_window(c, origin_x, origin_y + 5*scale, 5*scale, True)
    draw_window(c, origin_x + 26*scale, origin_y + 25*scale, 6*scale, False)
    
    # Dimensions
    add_dimension(c, origin_x + 12*scale, origin_y - 15, "32'-0\"", 10)
    add_dimension(c, origin_x - 30, origin_y + 12.5*scale, "25'-0\"", 10)
    
    # Additional details
    c.setFont("Helvetica", 8)
    c.drawString(origin_x, origin_y - 40, "Wall Heights: 8'-0\" | Interior Wall Thickness: 5\" | Exterior Wall Thickness: 6\"")
    
    c.save()
    print(f"Created: {filename}")

# Generate all floor plans
if __name__ == "__main__":
    print("Generating US Residential Floor Plan PDFs for Drywall Estimation Testing...")
    print("=" * 70)
    
    create_single_story_3br()
    create_single_story_2br()
    create_two_story_4br()
    create_two_story_3br()
    create_apartment_1br()
    
    print("=" * 70)
    print("All 5 floor plans generated successfully!")
    print("\nFiles created:")
    print("1. floor_plan_1_single_story_3br.pdf - Single-Story 3BR Ranch (1,800 sq ft)")
    print("2. floor_plan_2_single_story_2br.pdf - Single-Story 2BR Bungalow (1,200 sq ft)")
    print("3. floor_plan_3_two_story_4br.pdf - Two-Story 4BR Colonial (2,400 sq ft)")
    print("4. floor_plan_4_two_story_3br.pdf - Two-Story 3BR Home (2,000 sq ft)")
    print("5. floor_plan_5_apartment_1br.pdf - 1BR Apartment (800 sq ft)")
