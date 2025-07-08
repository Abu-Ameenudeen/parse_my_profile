from bs4 import BeautifulSoup

# === Load and Parse HTML ===
def load_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return BeautifulSoup(file.read(), "lxml")

# === Extract Profile Info from One <div class="profile"> ===
def parse_profile(profile_div):
    name = profile_div.find("h1").text
    bio = profile_div.find("p", class_="bio").text
    skills = [li.text for li in profile_div.select("ul.skills li")]

    # Extract GitHub and Email from links
    github = None
    email = None
    for link in profile_div.find_all("a", href=True):
        href = link["href"]
        if href.startswith("https://github.com/"):
            github = href
        elif href.startswith("mailto:"):
            email = href.replace("mailto:", "")

    return {
        "name": name,
        "bio": bio,
        "skills": skills,
        "github": github,
        "email": email
    }

# === Print a Single Profile Nicely ===
def print_profile(profile_data, index):
    print(f"\n👤 Profile {index}")
    print(f"Name: {profile_data['name']}")
    print(f"Bio: {profile_data['bio']}")
    print("Skills:", ", ".join(profile_data["skills"]))
    print(f"GitHub: {profile_data['github']}")
    print(f"Email: {profile_data['email']}")

# === Main Execution ===
def main():
    soup = load_html("profile.html")
    profiles = soup.find_all("div", class_="profile")

    for i, profile_div in enumerate(profiles, start=1):
        profile_data = parse_profile(profile_div)
        print_profile(profile_data, i)

# === Run Script ===
if __name__ == "__main__":
    main()
