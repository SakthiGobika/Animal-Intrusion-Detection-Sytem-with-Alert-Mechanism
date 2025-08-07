class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def __str__(self):
        return f"{self.name} - Votes: {self.votes}"


class Voter:
    def __init__(self, username):
        self.username = username
        self.has_voted = False


class VotingSystem:
    def __init__(self):
        self.candidates = []
        self.voters = {}
        self.admin_password = "admin123"  # Change as needed

    def add_candidate(self, name):
        self.candidates.append(Candidate(name))
        print(f"✅ Candidate '{name}' added.")

    def register_voter(self, username):
        if username in self.voters:
            print("⚠️ Voter already registered.")
        else:
            self.voters[username] = Voter(username)
            print(f"✅ Voter '{username}' registered.")

    def cast_vote(self, username):
        if username not in self.voters:
            print("❌ Voter not registered.")
            return

        voter = self.voters[username]
        if voter.has_voted:
            print("⚠️ You have already voted.")
            return

        print("\n🗳️ Candidates:")
        for idx, candidate in enumerate(self.candidates, start=1):
            print(f"{idx}. {candidate.name}")

        try:
            choice = int(input("Enter the number of the candidate you want to vote for: "))
            if 1 <= choice <= len(self.candidates):
                self.candidates[choice - 1].votes += 1
                voter.has_voted = True
                print("✅ Vote cast successfully.")
            else:
                print("❌ Invalid choice.")
        except ValueError:
            print("❌ Please enter a valid number.")

    def show_results(self, password):
        if password != self.admin_password:
            print("❌ Incorrect admin password.")
            return

        print("\n📊 Voting Results:")
        for candidate in self.candidates:
            print(candidate)

        winner = max(self.candidates, key=lambda c: c.votes, default=None)
        if winner:
            print(f"\n🏆 Winner: {winner.name} with {winner.votes} votes!")

    def menu(self):
        while True:
            print("\n====== ONLINE VOTING SYSTEM ======")
            print("1. Register as Voter")
            print("2. Vote")
            print("3. View Results (Admin only)")
            print("4. Add Candidate (Admin only)")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                uname = input("Enter your username to register: ")
                self.register_voter(uname)

            elif choice == '2':
                uname = input("Enter your username to vote: ")
                self.cast_vote(uname)

            elif choice == '3':
                pwd = input("Enter admin password: ")
                self.show_results(pwd)

            elif choice == '4':
                pwd = input("Enter admin password: ")
                if pwd == self.admin_password:
                    cname = input("Enter candidate name: ")
                    self.add_candidate(cname)
                else:
                    print("❌ Incorrect password.")

            elif choice == '0':
                print("👋 Exiting Voting System. Thank you!")
                break

            else:
                print("❗ Invalid option. Try again.")


if __name__ == "__main__":
    system = VotingSystem()
    system.menu()
