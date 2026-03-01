# ohmlaw calculator program

A basic electronics unit calculation program developed in Python 3. This tool helps in calculating Voltage (V), Current (Amperes), Resistance (Ohms), Power (Watts), and Capacitance (Farads), making it useful for circuit designing and educational purposes.

## Features

- **Ohm's Law Calculations**: Calculate Voltage, Current, Resistance, and Power.
- **Circuit Analysis**: Supports calculations for Series and Parallel circuits.
- **Wide Range of Units**: Supports calculations with:
  - **Voltage**: V
  - **Current**: A (Amperes)
  - **Resistance**: ohm, kohm, Mohm
  - **Power**: W (Watts)
  - **Capacitance**: F, uF, nF, pF
- **Debian Linux Compatible**: Designed to run smoothly on Debian-based Linux distributions.

## Requirements

To run this program, you need:

- **Operating System**: Linux (Compatible with Debian-based distributions like Ubuntu, Debian, Kali, etc.)
- **Software**:
  - **Python 3**
  - **Git**

## Installation

Follow these steps to install the necessary requirements and the program:

1. **Update your system:**
   ```bash
   sudo apt update
   ```

2. **Install Python3 and Git:**
   ```bash
   sudo apt install python3 git
   ```

3. **Clone the repository:**
   ```bash
   git clone [INSERT REPOSITORY LINK HERE]
   ```

4. **Navigate to the project directory:**
   ```bash
   cd ohmlaw-calculator
   ```

## Usage

Run the program using the following command:

```bash
python3 ohmlaw-calculator.py
```

### How to Use

The program will prompt you to enter values, their identities (units), and an operator (calculation type).

1. **Enter the 1st Value**: Input the number.
2. **Enter the 1st Value Identity**: Input the unit (e.g., `V`, `A`, `ohm`).
3. **Enter the 2nd Value**: Input the number.
4. **Enter the 2nd Value Identity**: Input the unit.
5. **Enter the Operator**: Input the variable you want to calculate (e.g., `V`, `R`, `I`, `P`, `C`).

### ⚠️ IMPORTANT NOTE

**This program is strictly Case Sensitive.**

- **Operators** (Equation Names) must be entered in **CAPITAL LETTERS** (e.g., `R`, `V`, `I`, `P`).
- **Value Identities** (Units) must be entered in **CAPITAL LETTERS** for single-letter units (e.g., `V`, `A`, `W`).
- For multi-letter units (like `ohm`, `kohm`, `uF`), enter them exactly as required by the program logic (e.g., `ohm` is lowercase).

**Failure to use the correct case will result in an "Invalid operator" or "Invalid value" error.**
