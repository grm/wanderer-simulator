# Equipment Simulator

This project simulates the behavior of equipment through a Python application. It allows users to interact with the simulated equipment and test various methods.

## Project Structure

```
equipment-simulator
├── src
│   ├── main.py          # Entry point of the application
│   ├── equipment.py     # Contains the EquipmentSimulator class
│   └── tests
│       └── test_equipment.py  # Unit tests for EquipmentSimulator
├── requirements.txt     # Lists project dependencies
└── README.md            # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd equipment-simulator
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the equipment simulator, execute the following command:
```
python src/main.py
```

## Testing

To run the unit tests for the EquipmentSimulator class, use:
```
python -m unittest discover -s src/tests
```

## Features

- Initialize the equipment simulator
- Set home position
- Move to a specified position
- Get the current status of the equipment

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.