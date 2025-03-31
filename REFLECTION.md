# Challenges in Translating Requirements into Use Cases and Tests
Working on this project taught me how difficult it can be to turn requirements into detailed use cases and tests. At the start, I had a general idea of what features the app needed, like login, inventory management, and payment processing. But turning those big ideas into specific user stories, use case diagrams, and testable tasks was not easy.

One of the first challenges I faced was making sure I truly understood the requirements. Even though I was the only stakeholder, I had to put myself in the shoes of a business owner, customer, and admin. It was tricky to imagine how each user would interact with the system and what they would expect. I had to ask myself many questions and keep going back to the user goals to make sure the use cases made sense.

Another challenge was writing the use cases clearly. I had to describe each user’s steps in the system and show how they interacted with different features. Sometimes I used too much technical language or skipped steps that seemed obvious to me but might confuse someone else. This made me realize how important it is to write in a simple, clear way so that anyone can understand the process.

Creating test cases was also difficult. I had to make sure each use case could be tested with real conditions. For example, for the login feature, I had to think about what would happen if the user entered the wrong password or if the internet connection failed. This required a lot of attention to detail. I had to think about all the “what if” situations and make sure the app would handle them properly.

The use case diagram was helpful because it gave me a visual way to see all the actors and how they connect to the system. But using Mermaid.js to draw it came with its own problems because it doesn’t fully support all UML features. I had to find workarounds to show includes and relationships. It worked out in the end, but it took time to figure out.

Overall, this part of the project showed me how important it is to plan carefully. Requirements are just the start. Translating them into use cases and tests takes time, patience, and thinking through all the details. It also helped me improve my communication skills because I had to write everything in a way that made sense to others, even if they weren’t technical.


# Challenges in Prioritization, Estimation, and Aligning Agile with Stakeholder Needs
During this assignment, I learned how hard it can be to prioritize tasks, estimate effort, and follow Agile principles, especially when I am acting as the only stakeholder. In a real team, there would be people to help decide what’s most important, but here I had to make all the decisions myself.

One challenge was using the MoSCoW method (Must-have, Should-have, Could-have, Won’t-have). At first, everything felt like a must-have. It was hard to separate what was truly essential from what could wait. I had to think about the MVP — the Minimum Viable Product — and focus only on features that are needed for the system to work. For example, user login and payment processing were must-haves, but things like promotional messaging were not essential for the first version.

Estimating effort was another difficult part. I had to give story points or hours for each task. Since I’m working alone and still learning, it was hard to know how long something would take. I had to guess based on complexity, and sometimes I overestimated or underestimated. For example, setting up Firebase login took longer than I thought, while designing the dashboard layout was quicker. This helped me understand that estimation is a skill that improves with experience.

Aligning Agile practices with my work also came with challenges. In Agile, you often get feedback from the stakeholder, but since I was the only one, I had to give myself feedback. I used GitHub Projects to organize my tasks and created issues with priority and effort tags. I moved them across the board as I worked. Even though I had no team to discuss progress with, the board helped me stay focused and track my work.

One more difficulty was choosing what to work on first. Agile recommends selecting 4–6 user stories per sprint, so I had to pick from my backlog carefully. I chose the most connected and high-priority ones, like login, inventory, and payment. But it wasn’t always clear which tasks had dependencies, so I had to look back at my use case diagram and backlog table to decide.

In the end, this part of the project helped me understand the real-world problems of project planning. Prioritization, estimation, and planning sprints take practice. This assignment made me realize that Agile is flexible, but it still needs structure and clear thinking to make good progress.


# Challenges in Selecting and Customizing the Template
Initially, selecting a GitHub template felt overwhelming due to the variety available—each designed for a different workflow. The real challenge was identifying which one best aligned with our Agile team's needs without overcomplicating things. Templates like Team Planning and Iterative Development seemed powerful but came with layers of setup not immediately necessary for our project scope.

I chose the Kanban template because of its simplicity and its alignment with Agile principles like visual task tracking, limiting WIP, and encouraging continuous delivery. However, after choosing it, I quickly realized that customization was not as straightforward as Trello’s drag-and-drop editing. Adjusting columns, adding WIP limits, and linking existing GitHub Issues to the board required going beyond the UI and understanding GitHub’s project configuration settings. There was a learning curve in figuring out how to assign Issues correctly, update their statuses, and make sure they reflected on the board.

Another pain point was maintaining consistency across two boards (the original and the newly created Kanban board). Ensuring that the tasks from Assignment 6 were accurately migrated and linked to the board—not recreated—required trial and error. Assigning tasks using the @mention system was helpful, but only once I understood that assignees had to have access to the repo or board.

# Comparison: GitHub Kanban vs Trello vs Jira
In comparing GitHub to Trello and Jira, I found GitHub’s integration with code repositories to be its biggest strength. Being able to connect Issues, commits, pull requests, and project tracking in one ecosystem is invaluable for developers. However, it lacks the out-of-the-box clarity that tools like Trello provide.

Trello shines in ease of use and intuitive UI, making it ideal for non-technical teams or rapid brainstorming sessions. But it lacks tight integration with code or automated workflows unless you use external power-ups. On the other hand, Jira offers advanced customization, robust reporting tools, sprint planning features, and integrates well with large team operations—but comes with a steep learning curve and can be overwhelming for smaller teams or academic projects.

## Table 
| Feature             | GitHub (Kanban)                         | Trello                              | Jira                                |
|---------------------|------------------------------------------|--------------------------------------|-------------------------------------|
| Visual Workflow     | Visual columns and progress tracking     | Easy drag-and-drop boards            | Custom workflows per team           |
| Ease of Use         | Moderate (needs GitHub familiarity)      | Very beginner-friendly               | Complex, requires onboarding        |
| Code Integration    | Native GitHub Issue and PR integration   | Requires plugins                     | Strong (especially with Bitbucket)  |
| WIP Management      | Manual via columns and discipline        | No real WIP limit                    | Supports WIP rules and metrics      |
| Automation          | GitHub Actions and bots (not intuitive)  | Butler (limited but simple)          | Built-in advanced rules/triggers    |
| Team Assignment     | Uses @mentions and assignees             | Labels and checklists                | Role assignments, priorities        |
