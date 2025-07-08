from bs4 import BeautifulSoup

# Load the HTML file
with open("profile.html", "r", encoding="utf-8") as file:
    html = file.read()

# Parse using lxml parser
soup = BeautifulSoup(html, "lxml")

# Extract profile details
name = soup.find("h1").text
bio = soup.find("p", class_="bio").text
skills = [li.text for li in soup.select("ul.skills li")]
github = soup.find("a")["href"]

# Output
print(f"Name: {name}")
print(f"Bio: {bio}")
print("Skills:", ", ".join(skills))
print(f"GitHub: {github}")
