%%{init: {'theme': 'default'}}%%
flowchart TD
    subgraph User
        U1([Start]) --> U2[Enter username & password]
        U2 --> U3{Is input valid?}
        U3 -- No --> U4[Show error message]
        U4 --> U9([End])
    end

    subgraph System
        U3 -- Yes --> S1[Validate credentials]
        S1 --> S2{Are credentials correct?}
        S2 -- No --> S3[Return login error]
        S3 --> U9
        S2 -- Yes --> S4[Create session]
        S4 --> S5[Load dashboard & features]
        S5 --> U9
    end
