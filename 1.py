rez = int(input())
m_rez = 0

while rez != -1:
    rez = int(input())
    if m_rez < rez:
        m_rez = rez

print(m_rez)