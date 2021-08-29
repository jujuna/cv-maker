from fpdf import FPDF

class PDF(FPDF):
    def name(self,name):
        pdf.add_font('ArialUnicode', fname='Arial-Unicode-Regular.ttf', uni=True)
        pdf.set_font('ArialUnicode', '', 20)
        pdf.cell(10, 10, name)

    def info(self,email,addr,mob):
        pdf.set_font("ArialUnicode", "", size=12)

        pdf.cell(170, 10, email, align="R")
        pdf.image('e.png', x=195, y=12, w=0, h=6)

        pdf.cell(-0.1, 30, addr, align="R")
        pdf.image('m.png', x=196, y=21, w=0, h=6)

        pdf.cell(-0.1, 50, mob, align="R")
        pdf.image('l.png', x=195, y=30, w=0, h=6)

    def experience(self,experience):
        pdf.set_font("ArialUnicode", "",size=15)
        pdf.cell(-143,75,"გამოცდილება",align="R")

        pdf.set_line_width(1)
        pdf.line(50,52,11,52)

        pdf.set_font_size(12)
        pdf.set_y(53)
        pdf.multi_cell(73,7,experience)

    def education(self,edu):
        pdf.set_font("ArialUnicode", "", size=15)

        pdf.cell(0,60,'განათლება')

        pdf.set_line_width(1)
        pdf.line(50, 96, 11, 96)

        pdf.set_x(9)
        pdf.set_y(97)
        pdf.multi_cell(75,7,edu,align="L")
    def skills(self,skil):
        skill_list=skill.split()
        pdf.set_font("ArialUnicode", "", size=15)
        pdf.set_y(22)
        pdf.set_x(130)
        pdf.cell(0,50,"უნარები")
        pdf.line(132,53,180,53)

        x,y=22,5
        setx,sety=131,60
        pdf.set_fill_color(255, 204, 153)
        pdf.set_draw_color(255,153,153)
        pdf.set_font_size(10)
        for i in range(len(skill_list)):
            if i % 3 == 0 and i != 0:
                sety += 30
                setx = 131
            pdf.set_y(sety)
            pdf.set_x(setx)
            pdf.cell(x, y, skill_list[i], fill=True,  align="C")
            setx += 25

    def languages(self,lang):
        lang_list=lang.split()
        pdf.set_font("ArialUnicode", "", size=15)
        pdf.set_y(95)
        pdf.set_x(10)
        pdf.cell(0, 85, "ენები")
        pdf.set_draw_color(0,0,0)
        pdf.line(10, 145, 50, 145)
        pdf.set_font_size(10)
        x,y=22,10
        setx,sety=10,150

        for i in range(len(lang_list)):
            if i % 3 == 0 and i != 0:
                sety += 20
                setx = 10
            pdf.set_y(sety)
            pdf.set_x(setx)
            pdf.cell(x, y, lang_list[i], fill=True,  align="C")
            setx += 25



name=str(input('სახელი გვარი: '))
email=str(input('ემაილი: '))
mobile=str(input('ტელეფონი: '))
addr=str(input('მისამართი: '))
experience=str(input('გამოცდილება: '))
education=str(input('განათლება :'))
skill=str(input('უნარები (გამოიყენე დაშორებები): '))
lang=str(input('ენები (გამოიყენე დაშორებები): '))
pdf = PDF()
pdf.add_page()
pdf.name(name)
pdf.info(email,addr,mobile)
pdf.experience(experience)
pdf.education(education)
pdf.skills(skill)
pdf.languages(lang)
pdf.output('tuto3.pdf')