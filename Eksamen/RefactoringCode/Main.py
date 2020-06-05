

    list = []
    Frederik Lumberger = Member("Frederik Lumberger", "920328-0923", "true")

    
    


        List<Person> people = new ArrayList<>() {
            {

                add(new Member("Frederik Lumberger", "920328-0923", true));
                add(new Member("Nick", "293928-2392", true));
                add(new Member("Marc", "909823-2395", false));
                add(new Administration("Dude", "029396-2990", 37, 5, 23000));
                add(new Administration("Mate2", "029393-2890", 37, 5, 23000));
                add(new Administration("Mate3", "029391-2790", 37, 5, 23000));
                add(new Instructor("Mate", "092093-2309", 20, 456));
                add(new Instructor("Larman", "902382-9320", 37, 456));
                add(new Person("Frederick Lumberg", "209238-2303"));

            }
        };

        System.out.println("Fitness Employees");
        System.out.println("*".repeat(50));
        System.out.println("*".repeat(50));
        //Craetes a for each loop, assign them to p for each "people" found
        for (Person p : people) {
            if (p instanceof Employee) {
                if (p instanceof Administration) {
                    Administration a = (Administration) p;
                    System.out.println("\nName: " + a.getName() + "\nCpr: " + a.getCpr() + "\nSalary: " + a.getSalary() + "\nHours: " + a.getHours() + "\nVacation: " + a.getVacation());
                    continue;
                } else if (p instanceof Instructor) {
                    Instructor i = (Instructor) p;
                    System.out.println("\nName: " + i.getName() + "\nCpr: " + i.getCpr() + "\nSalary: " + i.getSalary() + "\nHours: " + i.getHours());
                    continue;
                }
                Employee e = (Employee) p;
                System.out.println("\nName: " + e.getName() + "\nCpr: " + e.getCpr() + "\nHours: " + e.getHours() + "\nSalary: " + e.getSalary());
            }
        }
        System.out.println("=".repeat(50));
        System.out.println("=".repeat(50));
        System.out.println("=".repeat(50));
        System.out.println("Fitness Members");
        System.out.println("*".repeat(50));
        System.out.println("*".repeat(50));
        for (Person p : people) {

            if (p instanceof Member) {
                Member m = (Member) p;
                System.out.println("\nName: " + m.getName() + "\nCpr: " + m.getCpr() + "\nMember: " + m.getMemberType() + "\nMonthly Fee: " + m.monthlyFee());
            }
        }
    }

}


