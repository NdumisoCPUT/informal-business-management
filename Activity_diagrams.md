%%{init: {'theme': 'default'}}%%
flowchart TD
    subgraph User
        A1([Start]) --> A2[Enter username & password]
        A2 --> A3{Is input valid?}
        A3 -- No --> A4[Show error message]
        A4 --> A5([End])
    end

    subgraph System
        A3 -- Yes --> B1[Validate credentials]
        B1 --> B2{Are credentials correct?}
        B2 -- No --> B3[Return login error]
        B3 --> A5
        B2 -- Yes --> B4[Create session]
        B4 --> B5[Load dashboard & features]
        B5 --> A5
    end
