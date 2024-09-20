# Defining the scope of our simulation

## Core Structure

### 1. Actors
- Each actor starts with an initial stake.
- Each actor has a probability of being faulty (binary or continuous).
- Actors can be added or removed from the system as the simulation proceeds.

### 2. Faulty Sets
- A list of faulty sets defines specific combinations of actors (single or multiple) that can be faulty during execution.
- Each faulty set has an associated probability of causing a fault.

### 3. Execution Rounds
- In each round, a random set of actors is selected to perform a task.
- If any subset of the selected actors matches a faulty set, the fault probability is checked.
- If the fault occurs (based on the probability), the task is considered faulty, and the actors in the faulty set are penalized (slashed).
- If no fault occurs, the task is successful, and all participating actors are rewarded.

### 4. Actor Lifecycle
- Actors are removed from the system if their stake reaches 0.
- New actors are introduced into the system at regular intervals, with a random fault probability assigned (from a Poisson distribution).

### 5. Tracking
- Track the global error rate across all rounds (percentage of faulty tasks).
- Track the evolution of each actor's stake over time.

---

## Scenarios Formalized

### Scenario 1: Binary Behavior, Single Actor Fault Sets
- **Description**: Actors are either always faulty or never faulty (probability of 0 or 1). Faulty sets are composed of single actors only.
- **Faulty Set**: A list of single actors, each with a fault probability of 0 or 1.
- **Fault Condition**: If the actor is in the selected task set and is in the faulty set, the task is faulty.

### Scenario 2: Non-Binary Behavior, Single Actor Fault Sets
- **Description**: Actors have a probability between 0 and 1 of being faulty. Faulty sets are still composed of single actors only.
- **Faulty Set**: A list of single actors, each with a fault probability ranging between 0 and 1.
- **Fault Condition**: If the actor is in the selected task set, their probability of fault is checked. If the fault occurs, the task is faulty.

### Scenario 3: Binary Behavior, Multi-Actor Fault Sets
- **Description**: Actors are either always faulty or never faulty (probability of 0 or 1). Faulty sets can be composed of single actors or combinations of actors.
- **Faulty Set**: A list of combinations of actors, each with a fault probability of 0 or 1.
- **Fault Condition**: If any subset of the selected task set matches a faulty set, the fault probability is checked. If the fault occurs, the task is faulty.

### Scenario 4: Non-Binary Behavior, Multi-Actor Fault Sets
- **Description**: Actors have a probability between 0 and 1 of being faulty. Faulty sets can be composed of single actors or combinations of actors.
- **Faulty Set**: A list of combinations of actors, each with a fault probability between 0 and 1.
- **Fault Condition**: If any subset of the selected task set matches a faulty set, the fault probability is checked. If the fault occurs, the task is faulty.
