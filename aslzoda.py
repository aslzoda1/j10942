## 1. Main Greeting
def main():
    print("🐍 Aslzoda Bozorboyeva - Advanced Python Automation")
    data_structures_demo()
    math_operations()
    lambda_filters()

# 2. Data Structures Demo
def data_structures_demo():
    user_profile = {"name": "Aslzoda", "role": "Android Architect", "age": 20}
    for key, value in user_profile.items():
        print(f"🔹 {key.capitalize()}: {value}")

# 3. Math & Logic
def math_operations():
    fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21]
    squares = [x**2 for x in fibonacci if x % 2 == 0]
    print(f"📈 Even Fibonacci squares: {squares}")

# 4. Filter and Mapping
def lambda_filters():
    skills = ["Kotlin", "Java", "Python", "Jetpack Compose", "C++"]
    tech_stack = list(filter(lambda x: len(x) > 4, skills))
    print(f"💻 Professional Stack: {tech_stack}")

if __name__ == "__main__":
    main()