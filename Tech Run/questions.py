# questions.py

# --- 100 DIGITAL LITERACY QUESTIONS ---
all_questions = [
    {
        "question": "Which computer component is called the 'brain' because it processes all instructions?",
        "options": ["CPU (Central Processing Unit)", "RAM (Random Access Memory)", "Hard Drive (Storage)", "GPU (Graphics Processing Unit)"],
        "answer": "CPU (Central Processing Unit)",
        "hint": "It's where calculations and decisions happen",
        "explanation": "The CPU (Central Processing Unit) is the primary component that executes most of the processing inside a computer. It interprets and carries out instructions from software, performs arithmetic and logical operations, and manages data flow between components. Modern CPUs contain billions of transistors and can perform trillions of calculations per second."
    },
    {
        "question": "RAM (Random Access Memory) is temporary memory. What happens to RAM data when computer power is turned off?",
        "options": ["All data is immediately lost", "Data is automatically saved to storage", "Data uploads to cloud storage", "Data freezes and recovers on restart"],
        "answer": "All data is immediately lost",
        "hint": "RAM needs constant electricity to remember",
        "explanation": "RAM (Random Access Memory) is volatile memory that requires constant electrical power to maintain stored information. When power is removed, all data in RAM is immediately lost. This differs from storage devices like hard drives and SSDs, which use non-volatile memory to preserve data without power."
    },
    {
        "question": "Where are your documents, photos, and operating system permanently stored?",
        "options": ["Hard Drive or SSD (Storage)", "RAM (Temporary Memory)", "CPU (Processor)", "Motherboard (Main Circuit Board)"],
        "answer": "Hard Drive or SSD (Storage)",
        "hint": "Long-term storage devices",
        "explanation": "Hard drives and SSDs provide non-volatile storage for permanent file retention. Traditional hard drives use magnetic platters that spin, while SSDs use flash memory chips with no moving parts. Both maintain data without power, making them ideal for long-term storage of operating systems, applications, and personal files."
    },
    {
        "question": "Why are SSDs (Solid State Drives) generally faster than HDDs (Hard Disk Drives)?",
        "options": ["No moving mechanical parts", "They are physically larger in size", "They use more electrical power", "Their disks spin at higher speeds"],
        "answer": "No moving mechanical parts",
        "hint": "HDDs have spinning disks and moving heads",
        "explanation": "SSDs outperform HDDs because they have no mechanical moving parts. HDDs rely on physical read/write heads that move across spinning platters, causing latency. SSDs use NAND flash memory that accesses data electronically, resulting in significantly faster read/write speeds, lower latency, better durability, and silent operation."
    },
    {
        "question": "What is the main purpose of a GPU (Graphics Processing Unit)?",
        "options": ["Rendering images, videos, and games", "Storing documents and files", "Connecting to Wi-Fi networks", "Loading the operating system"],
        "answer": "Rendering images, videos, and games",
        "hint": "Essential for gaming, video editing, and 3D graphics",
        "explanation": "The GPU specializes in rendering images, video, and animations. Unlike CPUs which handle diverse tasks, GPUs excel at parallel processing of graphical data. This makes them essential for gaming, video editing, 3D modeling, and machine learning applications where massive calculations are needed simultaneously."
    },
    {
        "question": "What is the main circuit board that connects all computer components together?",
        "options": ["Motherboard", "Keyboard", "Monitor", "Power Supply Unit"],
        "answer": "Motherboard",
        "hint": "Everything plugs into this board",
        "explanation": "The motherboard is the primary printed circuit board that connects all hardware components. It provides electrical connections for the CPU, RAM, storage devices, expansion cards, and peripherals. The motherboard also contains critical subsystems like the chipset, BIOS/UEFI firmware, and various connectors that enable communication between all parts."
    },
    {
        "question": "Which of these devices sends information INTO the computer?",
        "options": ["Mouse (for cursor movement)", "Speaker (for sound output)", "Monitor (for display output)", "Printer (for paper output)"],
        "answer": "Mouse (for cursor movement)",
        "hint": "Input devices let you control and interact with the computer",
        "explanation": "A mouse is an input device that converts physical movement into digital signals the computer can process. Input devices allow users to interact with and control computers by sending data. Other examples include keyboards, scanners, microphones, and cameras. Output devices like monitors and speakers receive data from the computer."
    },
    {
        "question": "Which device shows information FROM the computer to the user?",
        "options": ["Monitor (displays the screen)", "Keyboard (types text input)", "Microphone (records audio input)", "Scanner (digitizes document input)"],
        "answer": "Monitor (displays the screen)",
        "hint": "Output devices show or give you results from the computer",
        "explanation": "A monitor is an output device that displays visual information from the computer. Output devices present processed data in human-perceivable forms. This includes visual displays (monitors), audio outputs (speakers), printed materials (printers), and tactile feedback devices. They complete the human-computer interaction loop."
    },
    {
        "question": "What is a 'device driver' in computing?",
        "options": ["Software that tells hardware how to work", "A person who operates the computer", "A physical screwdriver tool", "A type of computer virus"],
        "answer": "Software that tells hardware how to work",
        "hint": "Connects the operating system to specific hardware devices",
        "explanation": "A driver is specialized software that enables the operating system to communicate with hardware devices. It translates generic OS commands into device-specific instructions. Without proper drivers, hardware like printers, graphics cards, or network adapters cannot function correctly. Drivers ensure compatibility and optimal performance."
    },
    {
        "question": "What does the PSU (Power Supply Unit) do in a computer?",
        "options": ["Converts wall power for computer use", "Generates internet connection", "Stores data permanently", "Cools the CPU processor"],
        "answer": "Converts wall power for computer use",
        "hint": "It plugs into the electrical outlet and powers all components",
        "explanation": "The PSU converts alternating current (AC) from wall outlets into stable direct current (DC) voltages required by computer components. It provides different voltage rails (+12V, +5V, +3.3V) and includes safety features like overload protection. A quality PSU is essential for system stability and longevity."
    },
    {
        "question": "In computing, what is 'the Cloud'?",
        "options": ["Internet servers you access remotely", "A weather simulation program", "The inside of a computer case", "A type of wireless mouse"],
        "answer": "Internet servers you access remotely",
        "hint": "Storing files online instead of on your local computer",
        "explanation": "Cloud computing refers to delivering computing services—servers, storage, databases, networking, software—over the Internet. Instead of owning physical infrastructure, users access resources on-demand from remote data centers. This enables scalability, cost-efficiency, and accessibility from anywhere with internet connectivity."
    },
    {
        "question": "When logging into a website, which protocol is safer for your password: HTTP or HTTPS?",
        "options": ["HTTPS (encrypted connection)", "HTTP (unencrypted connection)", "Both are equally safe", "Neither is safe for passwords"],
        "answer": "HTTPS (encrypted connection)",
        "hint": "Look for the padlock icon and 'https://' in your browser address bar",
        "explanation": "HTTPS (Hypertext Transfer Protocol Secure) encrypts data between your browser and websites using TLS/SSL protocols. This prevents eavesdropping, data tampering, and man-in-the-middle attacks. HTTP sends data in plain text, making it vulnerable to interception. Always verify HTTPS when entering sensitive information."
    },
    {
        "question": "What is 'phishing' in cybersecurity?",
        "options": ["Tricking people into revealing sensitive information", "Catching fish using computer games", "A type of computer virus", "A PHP programming technique"],
        "answer": "Tricking people into revealing sensitive information",
        "hint": "Fake emails pretending to be from banks or trusted companies",
        "explanation": "Phishing is a cyberattack where attackers impersonate legitimate entities to steal sensitive information like login credentials, credit card numbers, or personal data. These attacks typically use deceptive emails, messages, or websites that appear genuine. Phishing exploits human psychology rather than technical vulnerabilities."
    },
    {
        "question": "What is the main purpose of a computer firewall?",
        "options": ["Blocks unauthorized network access", "Cools down overheating computers", "Speeds up Wi-Fi connections", "Deletes unwanted files automatically"],
        "answer": "Blocks unauthorized network access",
        "hint": "Acts like a security guard for your network connection",
        "explanation": "A firewall monitors and controls incoming/outgoing network traffic based on predetermined security rules. It acts as a barrier between trusted internal networks and untrusted external networks (like the Internet). Firewalls can be hardware-based, software-based, or cloud-based, and are essential for network security."
    },
    {
        "question": "What does 'encryption' do to data?",
        "options": ["Scrambles it so only authorized people can read it", "Permanently deletes it", "Creates backup copies of it", "Makes internet faster for it"],
        "answer": "Scrambles it so only authorized people can read it",
        "hint": "Turns readable text into secret code that needs a key to decode",
        "explanation": "Encryption converts plaintext into ciphertext using mathematical algorithms and cryptographic keys. Only authorized parties with the correct key can decrypt and read the original data. Encryption protects data confidentiality during storage and transmission, forming the foundation of modern digital security and privacy."
    },
    {
        "question": "What is a VPN (Virtual Private Network) primarily used for?",
        "options": ["Hides your location and encrypts internet traffic", "Makes your computer screen brighter", "Downloads more RAM memory", "Makes printing documents faster"],
        "answer": "Hides your location and encrypts internet traffic",
        "hint": "Creates a secure tunnel for your internet connection",
        "explanation": "A VPN creates an encrypted tunnel between your device and a remote server, masking your IP address and location. This protects your online privacy, secures data on public Wi-Fi, bypasses geographical restrictions, and prevents tracking by ISPs or advertisers. VPNs are essential for secure remote work."
    },
    {
        "question": "How does Wi-Fi transmit data between devices wirelessly?",
        "options": ["Using radio waves", "Using laser beams", "Using sound waves", "Through invisible physical cables"],
        "answer": "Using radio waves",
        "hint": "Similar to radio but with different frequencies for data",
        "explanation": "Wi-Fi uses radio frequency waves (typically 2.4 GHz and 5 GHz bands) to wirelessly transmit data between devices. These radio signals are modulated to carry digital information through the air. Wi-Fi enables local area networking without cables, with standards like Wi-Fi 6 offering speeds up to 9.6 Gbps."
    },
    {
        "question": "What is a web browser's main function?",
        "options": ["Views and displays web pages", "Is the same as the internet itself", "Is a search engine", "Is a Wi-Fi router"],
        "answer": "Views and displays web pages",
        "hint": "Examples: Google Chrome, Mozilla Firefox, Microsoft Edge, Safari",
        "explanation": "A web browser is application software that retrieves, renders, and displays content from the World Wide Web. It interprets HTML, CSS, and JavaScript to present web pages, handles user interactions, manages cookies and cache, and provides security features. Popular browsers include Chrome, Firefox, Safari, and Edge."
    },
    {
        "question": "What device connects your home network to your Internet Service Provider (ISP)?",
        "options": ["Modem", "Network Switch", "USB Hub", "Wi-Fi Repeater"],
        "answer": "Modem",
        "hint": "Translates signals from the street cables to your home network",
        "explanation": "A modem (modulator-demodulator) converts digital data from computers into analog signals for transmission over telephone/cable lines, and vice versa. It serves as the gateway between your local network and your Internet Service Provider's infrastructure. Modems establish the physical internet connection that routers then distribute."
    },
    {
        "question": "What is Two-Factor Authentication (2FA)?",
        "options": ["Password + temporary code (extra security)", "Two different passwords", "Logging in twice with same password", "Sharing your account with someone else"],
        "answer": "Password + temporary code (extra security)",
        "hint": "Extra security step beyond just a password",
        "explanation": "2FA requires two different authentication factors: something you know (password), something you have (phone/security key), or something you are (biometrics). This layered security makes unauthorized access significantly harder even if passwords are compromised. 2FA is now standard for securing important accounts."
    },
    {
        "question": "What is an Operating System (OS)?",
        "options": ["Software that manages hardware and runs applications", "A web browser like Chrome", "A word processor like Microsoft Word", "A video game"],
        "answer": "Software that manages hardware and runs applications",
        "hint": "Examples: Windows, macOS, Linux, Android, iOS",
        "explanation": "An OS is system software that manages computer hardware, software resources, and provides services for applications. It handles memory management, process scheduling, file systems, device drivers, security, and user interfaces. The OS acts as an intermediary between users/applications and the computer hardware."
    },
    {
        "question": "What does 'open source' mean for software?",
        "options": ["Source code is publicly available to view and modify", "The software costs money to use", "The software is broken or buggy", "The software has no password protection"],
        "answer": "Source code is publicly available to view and modify",
        "hint": "Examples: Linux operating system, Firefox browser, Python language",
        "explanation": "Open source software has source code that anyone can inspect, modify, and distribute. This promotes collaboration, transparency, and community-driven development. Open source licenses grant users freedom to use, study, change, and share the software. Examples include Linux, Apache, MySQL, Python, and Firefox."
    },
    {
        "question": "In programming, what is a 'bug'?",
        "options": ["An error or flaw in the code", "A hardware feature", "A type of computer virus", "A fast processor"],
        "answer": "An error or flaw in the code",
        "hint": "Causes programs to crash or behave unexpectedly",
        "explanation": "A bug is a flaw, error, or defect in software or hardware that causes incorrect or unexpected results. Bugs can range from minor graphical glitches to critical security vulnerabilities. The term originated when a moth caused a malfunction in the Harvard Mark II computer, popularized by Grace Hopper."
    },
    {
        "question": "What does GUI stand for in computing?",
        "options": ["Graphical User Interface", "Global Unit Interface", "General User Input", "Gaming User Interface"],
        "answer": "Graphical User Interface",
        "hint": "Uses icons, windows, and mouse instead of typing text commands",
        "explanation": "A GUI allows users to interact with electronic devices through graphical icons and visual indicators, as opposed to text-based command-line interfaces. GUIs use windows, icons, menus, and pointers (WIMP) to make computers more accessible. The first commercial GUI was Apple's Macintosh in 1984."
    },
    {
        "question": "What is a 'pixel' on a digital screen?",
        "options": ["The smallest unit of a digital image", "A type of computer cable", "A programming language", "A sound wave measurement"],
        "answer": "The smallest unit of a digital image",
        "hint": "Screens are made of millions of these tiny colored dots",
        "explanation": "A pixel (picture element) is the smallest controllable element of a digital image or display. Each pixel contains color information (typically red, green, and blue values) that combine to form complete images. Screen resolution is measured in pixels (e.g., 1920×1080 means 2+ million pixels)."
    },
    {
        "question": "Which file extension is typically used for images?",
        "options": [".jpg or .jpeg", ".mp3 (audio)", ".txt (text)", ".exe (executable)"],
        "answer": ".jpg or .jpeg",
        "hint": "Common for photos and pictures",
        "explanation": "JPG/JPEG (Joint Photographic Experts Group) is a commonly used lossy compression format for digital images. It balances file size and quality well for photographs. Other image formats include PNG (lossless with transparency), GIF (animations), and BMP (uncompressed). File extensions help identify file types."
    },
    {
        "question": "What does the keyboard shortcut Ctrl+C do?",
        "options": ["Copies selected content", "Cuts selected content", "Pastes copied content", "Closes the current window"],
        "answer": "Copies selected content",
        "hint": "C for Copy - stores content without removing it",
        "explanation": "Ctrl+C copies selected content to the clipboard without removing it from the source. This universal keyboard shortcut works across most operating systems and applications. The clipboard temporarily stores data for transfer between applications or locations. Related shortcuts include Ctrl+X (Cut) and Ctrl+V (Paste)."
    },
    {
        "question": "What does the keyboard shortcut Ctrl+V do?",
        "options": ["Pastes copied content", "Prints the document", "Plays media", "Views document properties"],
        "answer": "Pastes copied content",
        "hint": "V like inserting - puts copied content at cursor location",
        "explanation": "Ctrl+V inserts content from the clipboard at the current cursor position. This completes the copy-paste workflow essential for productivity. The clipboard can hold various data types including text, images, and files. Modern systems maintain clipboard history for multiple items."
    },
    {
        "question": "What does the keyboard shortcut Ctrl+Z do?",
        "options": ["Undoes the last action", "Redoes the last action", "Zooms in or out", "Puts computer to sleep"],
        "answer": "Undoes the last action",
        "hint": "Z for going back - reverses your last change",
        "explanation": "Ctrl+Z reverses the last action, providing error recovery in applications. This vital undo functionality allows users to experiment without permanent consequences. Most applications support multiple undo levels. The complementary Ctrl+Y or Ctrl+Shift+Z typically performs Redo."
    },
    {
        "question": "What is 'binary code' in computing?",
        "options": ["0s and 1s (base-2 number system)", "English text data", "Picture image data", "A type of keyboard layout"],
        "answer": "0s and 1s (base-2 number system)",
        "hint": "Fundamental language computers understand",
        "explanation": "Binary is a base-2 numeral system using only 0 and 1 to represent all data and instructions in computing. These bits correspond to electrical states (off/on) in transistors. Groups of bits form bytes (8 bits), which represent characters, numbers, or instructions. All digital data ultimately exists as binary."
    },
    {
        "question": "In Python programming, what does print() do?",
        "options": ["Outputs text to the console", "Prints to a physical printer", "Saves a game progress", "Deletes a line of code"],
        "answer": "Outputs text to the console",
        "hint": "Shows information on screen for debugging or display",
        "explanation": "The print() function outputs text or variables to the standard output (usually the console/terminal). It's essential for debugging, displaying results, and user interaction. In Python 3, print() is a built-in function that can format output, write to files, and handle various data types."
    },
    {
        "question": "In programming, what is a 'variable'?",
        "options": ["Stores a value that can change", "A value that never changes", "A logic error in code", "A graphics card component"],
        "answer": "Stores a value that can change",
        "hint": "Like x = 5 - a named container for data",
        "explanation": "A variable is a named storage location in memory that holds data values. Variables allow programs to store, retrieve, and manipulate data dynamically. They have data types (integer, string, etc.), names, and values that can change during execution. Proper variable naming is crucial for readable code."
    },
    {
        "question": "In programming, what is a 'string'?",
        "options": ["Text data (characters)", "Numerical data", "A list of items", "A repeating loop"],
        "answer": "Text data (characters)",
        "hint": "Wrapped in quotes like 'Hello' or 'Python'",
        "explanation": "A string is a sequence of characters used to represent text. In Python, strings are immutable sequences enclosed in single or double quotes. Strings support operations like concatenation, slicing, formatting, and searching. They're fundamental for handling text data, user input, and output formatting."
    },
    {
        "question": "In programming, what is an 'integer'?",
        "options": ["A whole number (no decimals)", "A decimal number", "Text data", "A file object"],
        "answer": "A whole number (no decimals)",
        "hint": "Examples: 1, 10, 500, -25",
        "explanation": "An integer is a whole number without fractional components. Integers can be positive, negative, or zero. They're used for counting, indexing, and mathematical operations. Programming languages typically offer various integer types (int, long) with different ranges. Integer arithmetic is faster than floating-point."
    },
    {
        "question": "In Python, what character starts a single-line comment?",
        "options": ["# (hash symbol)", "// (double slash)", "/* (slash star)", "-- (double dash)"],
        "answer": "# (hash symbol)",
        "hint": "Lines starting with this are ignored by Python",
        "explanation": "In Python, the hash symbol (#) begins a single-line comment. Everything following # on that line is ignored by the interpreter. Comments document code functionality, explain complex logic, or temporarily disable code. Multi-line comments use triple quotes (''' or \"). Good commenting improves code maintainability."
    },
    {
        "question": "In programming, what is a 'loop'?",
        "options": ["Repeats code multiple times", "Stops the program", "A broken web link", "A type of variable"],
        "answer": "Repeats code multiple times",
        "hint": "Performs the same action many times automatically",
        "explanation": "Loops repeatedly execute code blocks until conditions are met. 'For' loops iterate over sequences (like lists), while 'while' loops continue while conditions remain true. Loops enable efficient processing of multiple items, automation of repetitive tasks, and implementation of algorithms. Proper loop control prevents infinite loops."
    },
    {
        "question": "In programming, what does 'if/else' do?",
        "options": ["Makes decisions based on conditions", "Repeats code forever", "Imports a library", "Draws a circle graphic"],
        "answer": "Makes decisions based on conditions",
        "hint": "IF it's raining, take umbrella ELSE don't take umbrella",
        "explanation": "If/else statements create conditional branching in programs. They evaluate Boolean expressions to determine which code blocks execute. This enables programs to make decisions, handle different scenarios, and respond dynamically to input. Nested if/elif/else structures handle complex decision trees."
    },
    {
        "question": "In computer science, what is an 'algorithm'?",
        "options": ["Step-by-step instructions to solve a problem", "A very fast computer", "A musical rhythm", "A type of computer monitor"],
        "answer": "Step-by-step instructions to solve a problem",
        "hint": "Like a recipe for a computer to follow",
        "explanation": "An algorithm is a finite sequence of well-defined instructions for solving problems or performing computations. Algorithms must be unambiguous, have defined inputs/outputs, and terminate. They're fundamental to computer science, with examples including sorting, searching, and pathfinding algorithms. Efficiency is measured in time/space complexity."
    },
    {
        "question": "In programming, what is a 'function'?",
        "options": ["Reusable block of code that performs a task", "A program crash", "A computer virus", "A messy file organization"],
        "answer": "Reusable block of code that performs a task",
        "hint": "Define once, use many times throughout your program",
        "explanation": "A function is a named, reusable code block that performs a specific task. Functions accept parameters, return values, and promote modular, maintainable code. They enable code reuse, abstraction, and organization. Built-in functions come with languages, while user-defined functions implement custom logic."
    },
    {
        "question": "In programming, which operator checks if two values are equal?",
        "options": ["== (double equals)", "= (single equals)", "<> (angle brackets)", ">< (reverse brackets)"],
        "answer": "== (double equals)",
        "hint": "Single '=' assigns values, double '==' compares values",
        "explanation": "The equality operator (==) compares two values, returning True if equal, False otherwise. This differs from assignment (=) which assigns values. Most languages also provide inequality (!=), strict equality (===), and relational operators (<, >, <=, >=). Understanding operator differences prevents common bugs."
    },
    {
        "question": "In programming, what is a 'Boolean' value?",
        "options": ["True or False (yes/no logic)", "A large number", "A text sentence", "A decimal number"],
        "answer": "True or False (yes/no logic)",
        "hint": "Represents yes/no, on/off, true/false decisions",
        "explanation": "Boolean is a data type with only two possible values: True and False. Named after mathematician George Boole, Boolean algebra underpins digital logic and programming conditions. Booleans control program flow through conditional statements and logical operations (AND, OR, NOT). They represent binary states in computing."
    },
    {
        "question": "What is HTML used for in web development?",
        "options": ["Structures web page content", "Performs mathematical calculations", "Creates video games", "Manages databases"],
        "answer": "Structures web page content",
        "hint": "Builds the skeleton or structure of websites",
        "explanation": "HTML (HyperText Markup Language) defines web page structure using elements/tags. It creates headings, paragraphs, links, images, forms, and other content containers. HTML provides semantic meaning to content, which browsers render and search engines index. HTML5 added multimedia, graphics, and improved semantics."
    },
    {
        "question": "What is CSS used for in web development?",
        "options": ["Styles and designs web pages", "Sends email messages", "Handles server logic", "Stores user passwords"],
        "answer": "Styles and designs web pages",
        "hint": "Makes HTML look good with colors, layouts, fonts",
        "explanation": "CSS (Cascading Style Sheets) controls visual presentation of HTML documents. It handles layout, colors, fonts, spacing, animations, and responsiveness. CSS separates content from presentation, enabling consistent styling across multiple pages. Modern CSS includes Flexbox, Grid, and custom properties for sophisticated layouts."
    },
    {
        "question": "Which brackets does Python use for lists?",
        "options": ["[] (square brackets)", "{} (curly braces)", "() (parentheses)", "<> (angle brackets)"],
        "answer": "[] (square brackets)",
        "hint": "Square brackets for ordered collections",
        "explanation": "Python uses square brackets [] for lists, which are ordered, mutable sequences. Lists can contain mixed data types, support indexing/slicing, and provide methods for manipulation. Other bracket types: parentheses () for tuples and function calls, curly braces {} for dictionaries and sets. Proper bracket usage is syntax-critical."
    },
    {
        "question": "In programming, what is 10 + 5?",
        "options": ["15 (addition result)", "105 (concatenation)", "50 (multiplication)", "Error (type mismatch)"],
        "answer": "15 (addition result)",
        "hint": "Simple arithmetic addition",
        "explanation": "In programming, the + operator performs addition on numeric operands. 10 + 5 evaluates to 15. The + operator is overloaded in some languages: with strings it performs concatenation ('10' + '5' = '105'). Understanding operator behavior with different data types prevents unexpected results."
    },
    {
        "question": "In Python, what does 'import random' do?",
        "options": ["Loads the random number module", "Picks a random number immediately", "Causes the app to crash", "Does nothing by itself"],
        "answer": "Loads the random number module",
        "hint": "Gives access to random functions like random.randint()",
        "explanation": "The import statement loads Python modules containing reusable code. 'import random' provides functions for generating pseudo-random numbers, selections, and shuffling. Common functions: random.randint(), random.choice(), random.shuffle(). Importing expands language capabilities without rewriting functionality."
    },
    {
        "question": "In programming, what is a 'syntax error'?",
        "options": ["Code grammar is wrong", "Computer is overheating", "Internet is disconnected", "Hard drive is full"],
        "answer": "Code grammar is wrong",
        "hint": "Missing parenthesis, incorrect indentation, or misspelled keyword",
        "explanation": "Syntax errors occur when code violates language grammar rules, preventing interpretation/compilation. Common causes: missing parentheses, incorrect indentation, misspelled keywords, or invalid characters. Unlike runtime errors, syntax errors are caught before execution. Careful coding and IDE tools help avoid them."
    },
    {
        "question": "Which of these is a programming language?",
        "options": ["Python", "Cobra (snake)", "Viper (snake)", "Anaconda (snake)"],
        "answer": "Python",
        "hint": "Both a snake and a popular programming language",
        "explanation": "Python is a high-level, interpreted programming language known for readability and versatility. It supports multiple paradigms and has extensive libraries. The other options are snake species (though Anaconda is also a Python distribution). Programming languages provide syntax and semantics for writing executable instructions."
    },
    {
        "question": "What does IoT (Internet of Things) refer to?",
        "options": ["Internet-connected smart devices", "Input of Text systems", "Internal Technology", "Image of Time systems"],
        "answer": "Internet-connected smart devices",
        "hint": "Smart home devices, wearables, connected appliances",
        "explanation": "IoT refers to interconnected physical devices with sensors, software, and network connectivity that collect and exchange data. Examples: smart thermostats, wearables, industrial sensors. IoT enables automation, remote monitoring, and data-driven decision making across industries like healthcare, agriculture, and manufacturing."
    },
    {
        "question": "What is a 'server' in computing?",
        "options": ["Provides data/services to other computers", "A restaurant waiter", "A computer keyboard", "A monitor screen"],
        "answer": "Provides data/services to other computers",
        "hint": "Serves websites, files, or applications to clients",
        "explanation": "A server is a computer or system that provides resources, services, or data to client devices over a network. Server types include web servers, file servers, database servers, and application servers. Servers typically have robust hardware, run server operating systems, and operate continuously to ensure availability."
    },
    {
        "question": "What does a '404 Error' mean on a website?",
        "options": ["Page Not Found", "Server Overheated", "Internet Disconnected", "Virus Detected"],
        "answer": "Page Not Found",
        "hint": "The server couldn't find the requested page",
        "explanation": "HTTP 404 is a client error status code indicating the server couldn't find the requested resource. Common causes: broken links, deleted pages, or incorrect URLs. Unlike server errors (5xx), 404 errors mean the server is reachable but the specific content isn't available. Custom 404 pages improve user experience."
    },
    {
        "question": "What are browser 'cookies'?",
        "options": ["Small files that save website preferences", "A type of computer virus", "A form of online advertising", "A snack for programmers"],
        "answer": "Small files that save website preferences",
        "hint": "Help websites remember your login or preferences",
        "explanation": "Cookies are small text files websites store on your device to remember stateful information. They maintain login sessions, store preferences, track activity, and enable personalized experiences. Cookies can be session-based (deleted on browser close) or persistent (expire on set date). Privacy regulations govern cookie usage."
    },
    {
        "question": "Which typically downloads faster: local server or distant server?",
        "options": ["Local server (closer)", "Distant server (far away)", "Same speed regardless", "Upload is always faster"],
        "answer": "Local server (closer)",
        "hint": "Data travels physical distance through cables",
        "explanation": "Local servers provide faster downloads due to reduced latency and fewer network hops. Data transmission speed is limited by physics—signals travel through cables at about 2/3 light speed. Greater distances increase round-trip time, packet loss, and congestion. Content Delivery Networks (CDNs) mitigate this with globally distributed servers."
    },
    {
        "question": "What is 'buffering' when streaming video?",
        "options": ["Pre-loads video data to prevent interruptions", "Cleans the screen display", "Deletes old video files", "Encrypts video data"],
        "answer": "Pre-loads video data to prevent interruptions",
        "hint": "Builds a buffer of pre-downloaded content",
        "explanation": "Buffering downloads and stores media content in advance of playback to ensure smooth streaming despite network fluctuations. The buffer acts as a reservoir—filling during fast connections and emptying during playback. Larger buffers prevent interruptions but increase initial wait time. Adaptive streaming adjusts buffer size dynamically."
    },
    {
        "question": "What is a browser 'home page'?",
        "options": ["First page that opens when starting browser", "Your Facebook profile page", "Your computer desktop background", "Google.com search page"],
        "answer": "First page that opens when starting browser",
        "hint": "Customizable in browser settings",
        "explanation": "The home page is the default webpage that loads when opening a browser. Users can set it to frequently visited sites, search engines, or blank pages. Home pages serve as starting points for browsing sessions. Modern browsers often combine home pages with new tab pages showing recent sites and bookmarks."
    },
    {
        "question": "What is a 'hyperlink' on a webpage?",
        "options": ["Clickable link to another page", "A high-speed internet cable", "A super-fast computer", "A type of programming code"],
        "answer": "Clickable link to another page",
        "hint": "Usually blue and underlined text you can click",
        "explanation": "A hyperlink (link) connects web resources, allowing navigation between pages. Links use anchor tags (<a>) in HTML with href attributes specifying destinations. They enable the interconnected nature of the World Wide Web. Links can point to different sections, pages, sites, or file downloads."
    },
    {
        "question": "What does Refresh (F5) do in a web browser?",
        "options": ["Reloads the current page", "Deletes browsing history", "Restarts the computer", "Closes the current tab"],
        "answer": "Reloads the current page",
        "hint": "Useful if page is stuck or not loading correctly",
        "explanation": "Refreshing reloads the current webpage, requesting the latest version from the server. This updates dynamic content, clears display errors, and re-executes scripts. Shift+Refresh typically bypasses cache to force complete reload. Browser refresh is essential for web development and viewing real-time data."
    },
    {
        "question": "What is 'Incognito' or 'Private Browsing' mode?",
        "options": ["No local history or cookies saved", "Makes you invisible to your ISP", "Provides complete virus protection", "Makes internet connection faster"],
        "answer": "No local history or cookies saved",
        "hint": "Browser forgets your activity but your ISP still sees it",
        "explanation": "Incognito/Private browsing prevents local storage of history, cookies, and form data during the session. However, it doesn't anonymize your IP address, hide activity from employers/ISPs, or provide comprehensive privacy protection. Useful for shared computers or avoiding persistent tracking on your device."
    },
    {
        "question": "What is a 'domain name' for a website?",
        "options": ["Human-readable website address", "IP address numbers", "Account password", "Browser name"],
        "answer": "Human-readable website address",
        "hint": "Easier to remember than numbers like 192.168.1.1",
        "explanation": "Domain names are human-readable addresses mapped to IP addresses via DNS. They follow hierarchical structure: top-level domains (.com, .org), second-level domains (google), and subdomains (mail.google). Domain registration is managed by ICANN-accredited registrars. Domains make the web accessible without memorizing numeric IPs."
    },
    {
        "question": "What browser icon indicates a secure website connection?",
        "options": ["Padlock icon", "Red shield icon", "Smiley face icon", "Blinking cursor"],
        "answer": "Padlock icon",
        "hint": "Means the site uses HTTPS encryption",
        "explanation": "The padlock icon in browser address bars indicates HTTPS encryption with valid SSL/TLS certificates. This ensures data integrity and confidentiality between user and website. Modern browsers also display 'Secure' labels and highlight insecure sites. Always verify security indicators before entering sensitive information."
    },
    {
        "question": "What is 'ransomware' malware?",
        "options": ["Locks files and demands money", "Free useful software", "Antivirus protection", "Secure backup system"],
        "answer": "Locks files and demands money",
        "hint": "Encrypts your files until you pay ransom (never pay!)",
        "explanation": "Ransomware encrypts victims' files and demands payment for decryption keys. It spreads via phishing, exploits, or malicious downloads. Recovery without backups is difficult; paying doesn't guarantee restoration. Prevention includes regular backups, updates, antivirus, and user education. Ransomware attacks target individuals and organizations."
    },
    {
        "question": "Why should you regularly update software?",
        "options": ["Fixes security vulnerabilities", "Just for prettier looks", "Uses more disk space", "Slows down computer"],
        "answer": "Fixes security vulnerabilities",
        "hint": "Hackers often target old, unpatched software",
        "explanation": "Updates patch vulnerabilities, fix bugs, improve stability, and add features. Security patches close exploits that attackers use to compromise systems. Delaying updates increases attack surface. Automatic updates ensure timely protection, though testing may be needed in enterprise environments. Updates are cybersecurity fundamentals."
    },
    {
        "question": "Is it safe to do online banking on public Wi-Fi?",
        "options": ["No, hackers can intercept data", "Yes, always completely safe", "Only safe on mobile phones", "Yes if connection is fast"],
        "answer": "No, hackers can intercept data",
        "hint": "Public networks are often unencrypted",
        "explanation": "Public Wi-Fi lacks encryption, allowing attackers to intercept data through man-in-the-middle attacks. Banking requires secure connections; public networks risk credential theft. Use cellular data, VPNs, or wait for secure networks. Financial institutions use HTTPS, but additional precautions are necessary on untrusted networks."
    },
    {
        "question": "What is 'spyware' malware?",
        "options": ["Secretly records your activity", "James Bond movie software", "Security camera footage", "Antivirus software"],
        "answer": "Secretly records your activity",
        "hint": "Tracks keystrokes, screenshots, browsing habits",
        "explanation": "Spyware secretly monitors user activity, collecting data like keystrokes, screenshots, browsing history, and credentials. It can be installed via malicious downloads, vulnerabilities, or bundled with legitimate software. Spyware enables identity theft, corporate espionage, and privacy violations. Antispyware tools help detection and removal."
    },
    {
        "question": "What is the best protection against hard drive failure?",
        "options": ["Regular backups", "Hope it doesn't fail", "Keep computer always on", "Delete old files"],
        "answer": "Regular backups",
        "hint": "All drives eventually fail - be prepared",
        "explanation": "The 3-2-1 backup rule: 3 total copies, on 2 different media, with 1 offsite. Regular backups protect against hardware failure, ransomware, accidental deletion, and disasters. Backup solutions include external drives, network storage, and cloud services. Testing restoration ensures backup integrity when needed."
    },
    {
        "question": "What is 'social engineering' in cybersecurity?",
        "options": ["Manipulates people to get information", "Builds social networks", "Programs social robots", "Fixes social media computers"],
        "answer": "Manipulates people to get information",
        "hint": "Hacks humans instead of machines",
        "explanation": "Social engineering exploits human psychology rather than technical vulnerabilities. Techniques include phishing, pretexting, baiting, and tailgating. Attackers manipulate trust, authority, or urgency to bypass security. Defense requires awareness training, verification procedures, and skepticism toward unsolicited requests."
    },
    {
        "question": "What is a 'botnet' in cybersecurity?",
        "options": ["Network of infected computers", "Helpful robot assistant", "Fast internet network", "Fishing equipment network"],
        "answer": "Network of infected computers",
        "hint": "Your computer could be part of one without knowing",
        "explanation": "Botnets are networks of compromised devices controlled remotely by attackers. They perform distributed denial-of-service attacks, send spam, mine cryptocurrency, or steal data. Devices become bots via malware infections. Botnet detection requires network monitoring, antivirus, and intrusion prevention systems."
    },
    {
        "question": "What does antivirus software do?",
        "options": ["Scans for and removes malware", "Makes internet faster", "Downloads video games", "Cleans keyboard physically"],
        "answer": "Scans for and removes malware",
        "hint": "Like a vaccine for your computer",
        "explanation": "Antivirus software detects, prevents, and removes malicious software using signature-based detection, heuristics, and behavioral analysis. It provides real-time protection, scheduled scans, and quarantine capabilities. Modern antivirus includes firewall, anti-phishing, and ransomware protection layers. Regular updates maintain effectiveness."
    },
    {
        "question": "Why is '123456' a bad password choice?",
        "options": ["Easy to guess (most common)", "Too long to remember", "Contains only numbers", "Hard to type quickly"],
        "answer": "Easy to guess (most common)",
        "hint": "It's literally the most common password",
        "explanation": "'123456' tops lists of most used passwords, making it vulnerable to dictionary attacks. Strong passwords combine length (12+ characters), complexity (mixed case, numbers, symbols), and unpredictability. Password managers generate/store unique passwords. Multi-factor authentication adds essential protection layers."
    },
    {
        "question": "What should you do with a suspicious email requesting money?",
        "options": ["Mark as spam and delete", "Reply asking why they need it", "Click links to investigate", "Send money to be safe"],
        "answer": "Mark as spam and delete",
        "hint": "Never click links or reply to suspicious emails",
        "explanation": "Suspicious emails often contain phishing attempts, malware, or scams. Interacting confirms your address is active or installs malicious software. Report as spam/phishing to help filters improve. Verify unusual requests through separate communication channels. Never provide personal/financial information via email."
    },
    {
        "question": "Computer shuts down during gaming - what's the most likely cause?",
        "options": ["Overheating protection", "Too much disk space", "Mouse got unplugged", "Internet too fast"],
        "answer": "Overheating protection",
        "hint": "Modern CPUs shut down to prevent heat damage",
        "explanation": "Modern processors have thermal protection that triggers immediate shutdown at critical temperatures (typically 100°C+). Gaming stresses CPU/GPU, generating excess heat. Causes: dust-clogged heatsinks, failed fans, poor ventilation, or dried thermal paste. Cleaning and proper cooling prevent overheating issues."
    },
    {
        "question": "What is BIOS/UEFI in a computer?",
        "options": ["Starts before the operating system", "A computer game", "An internet browser", "A computer virus"],
        "answer": "Starts before the operating system",
        "hint": "Initializes hardware and tells computer how to boot",
        "explanation": "BIOS (Basic Input/Output System) and UEFI (Unified Extensible Firmware Interface) are low-level firmware that initializes hardware during boot. They perform POST (Power-On Self-Test), load bootloaders, and provide setup interfaces. UEFI replaces legacy BIOS with modern features like secure boot, faster startup, and larger drive support."
    },
    {
        "question": "Which cable carries both video and audio signals?",
        "options": ["HDMI (High-Definition Multimedia Interface)", "VGA (Video Graphics Array)", "Aux Cable (Audio Only)", "Power Cable (Electricity Only)"],
        "answer": "HDMI (High-Definition Multimedia Interface)",
        "hint": "Commonly used for TVs, monitors, and home theater",
        "explanation": "HDMI transmits uncompressed digital video and audio through a single cable. It supports high resolutions (up to 10K), HDR, ethernet, and ARC (Audio Return Channel). VGA carries only analog video, requiring separate audio. HDMI is standard for modern displays and home theater systems."
    },
    {
        "question": "What is screen 'resolution'?",
        "options": ["Pixel count (width × height)", "CPU processing speed", "Sound speaker volume", "Keyboard physical size"],
        "answer": "Pixel count (width × height)",
        "hint": "Higher numbers mean sharper, more detailed images",
        "explanation": "Resolution measures display dimensions in horizontal and vertical pixels (e.g., 1920×1080). Higher resolutions provide more detail and screen real estate. Common standards: HD (1280×720), Full HD (1920×1080), 4K (3840×2160), 8K (7680×4320). Resolution combined with screen size determines pixel density (PPI)."
    },
    {
        "question": "Why do computers have cooling fans?",
        "options": ["Remove heat from components", "Make pleasing computer noises", "Blow dust out of case", "Look cool aesthetically"],
        "answer": "Remove heat from components",
        "hint": "Electronics generate heat and can be damaged by overheating",
        "explanation": "Fans provide active cooling by moving air over heatsinks attached to hot components like CPUs and GPUs. As processor power increases, thermal management becomes critical. Advanced cooling includes liquid cooling, heat pipes, and vapor chambers. Proper cooling prevents thermal throttling and extends component lifespan."
    },
    {
        "question": "What is a computer 'peripheral'?",
        "options": ["External device (adds functionality)", "CPU (main processor)", "Internal hard drive", "Operating system software"],
        "answer": "External device (adds functionality)",
        "hint": "Plugs into computer like keyboard, mouse, printer",
        "explanation": "Peripherals expand computer capabilities beyond core functions. Input peripherals (keyboard, mouse, scanner) send data to computer. Output peripherals (monitor, printer, speakers) receive data. Storage peripherals (external drives) provide additional storage. Peripherals connect via USB, Bluetooth, or other interfaces."
    },
    {
        "question": "Which type of computer is more portable?",
        "options": ["Laptop (battery-powered)", "Desktop (stationary)", "Server (rack-mounted)", "Mainframe (room-sized)"],
        "answer": "Laptop (battery-powered)",
        "hint": "Runs on battery, has built-in screen and keyboard",
        "explanation": "Laptops integrate display, keyboard, trackpad, and battery into a single portable unit. They sacrifice some performance and upgradability for mobility. Modern laptops approach desktop performance while offering all-day battery life. Tablets and smartphones offer even greater portability with different trade-offs."
    },
    {
        "question": "What does Bluetooth technology do?",
        "options": ["Short-range wireless connections", "Global internet access", "Cools computer components", "Makes videos blue-tinted"],
        "answer": "Short-range wireless connections",
        "hint": "Used for headphones, keyboards, file transfers",
        "explanation": "Bluetooth creates personal area networks (PANs) for short-range wireless communication between devices. It operates in 2.4 GHz band with versions offering improved speed, range, and power efficiency. Common uses: audio devices, input devices, file transfer, IoT connections, and wireless peripherals."
    },
    {
        "question": "What does 'Airplane Mode' do on devices?",
        "options": ["Turns off wireless transmitters", "Makes phone fly in air", "Plays airplane sounds", "Charges battery to 100%"],
        "answer": "Turns off wireless transmitters",
        "hint": "Required during airplane takeoff and landing",
        "explanation": "Airplane mode disables all wireless transmitters: cellular, Wi-Fi, Bluetooth, GPS, and NFC. This prevents potential interference with aircraft systems and complies with aviation regulations. Some functions remain: offline apps, camera, music. Essential for flights and situations requiring radio silence."
    },
    {
        "question": "Mouse cursor freezing: which is NOT a likely cause?",
        "options": ["Monitor screen broken", "CPU at 100% usage", "Wireless mouse battery low", "Bad reflective surface"],
        "answer": "Monitor screen broken",
        "hint": "Broken monitor shows no image, but cursor still moves",
        "explanation": "Monitor failure affects display output, not cursor processing. Cursor freezing typically indicates system resource issues (CPU/memory overload), wireless interference, driver problems, or peripheral malfunctions. Troubleshooting steps: check batteries, surfaces, USB connections, system resources, and update drivers."
    },
    {
        "question": "In programming lists/arrays, what is the first item's index?",
        "options": ["0 (zero-based indexing)", "1 (one-based indexing)", "10 (ten-based indexing)", "A (letter-based indexing)"],
        "answer": "0 (zero-based indexing)",
        "hint": "Most programming languages start counting at 0",
        "explanation": "Zero-based indexing means the first element has index 0, second has 1, etc. This convention originates from how arrays are implemented in memory (element address = base address + index × element size). Most programming languages use zero-based indexing, though some (like MATLAB) use one-based."
    },
    {
        "question": "In programming, what is an 'infinite loop'?",
        "options": ["Repeats code forever (error)", "Runs code once only", "A very long cable", "A perfect circle shape"],
        "answer": "Repeats code forever (error)",
        "hint": "Usually causes program to freeze or crash",
        "explanation": "An infinite loop occurs when loop termination conditions are never met, causing endless repetition. This can crash programs or consume excessive resources. Common causes: missing increment statements, incorrect conditions, or break statement absence. Debugging requires checking loop logic and adding proper exit conditions."
    },
    {
        "question": "Float vs Integer in programming: what's the difference?",
        "options": ["Float has decimals, Integer doesn't", "Integer is text, Float is number", "Float is always bigger", "They are exactly the same"],
        "answer": "Float has decimals, Integer doesn't",
        "hint": "Float = Floating Point (decimal numbers)",
        "explanation": "Integers represent whole numbers; floats represent real numbers with decimal points. Floats use floating-point representation (sign, mantissa, exponent) allowing fractional values but with precision limitations. Operations: integers are exact, floats may have rounding errors. Choose type based on data requirements."
    },
    {
        "question": "What does file compression (.zip) do?",
        "options": ["Reduces file size", "Increases file size", "Deletes the files", "Plays music files"],
        "answer": "Reduces file size",
        "hint": "Packs data more efficiently to save space",
        "explanation": "Compression reduces file sizes by eliminating redundancy (lossless) or discarding less important data (lossy). Lossless (ZIP, PNG) allows perfect reconstruction; lossy (JPEG, MP3) trades quality for size. Compression saves storage, reduces transmission time, and enables streaming. Different algorithms suit different data types."
    },
    {
        "question": "What is the 'Recycle Bin' (Windows) or 'Trash' (Mac)?",
        "options": ["Holds deleted files temporarily", "Virus scanning tool", "Spam email folder", "Computer game"],
        "answer": "Holds deleted files temporarily",
        "hint": "Can restore files if deleted by mistake",
        "explanation": "The Recycle Bin (Windows) or Trash (macOS) provides safety net for file deletion. 'Deleted' files move here rather than being immediately erased. Users can restore accidentally deleted items or permanently delete by emptying the bin. The bin has configurable size limits and doesn't protect against low disk space deletions."
    },
    {
        "question": "What is a 'directory' (folder) in file systems?",
        "options": ["Organizes files into groups", "A phone book listing", "A direct cable connection", "A type of computer mouse"],
        "answer": "Organizes files into groups",
        "hint": "Contains files and other folders",
        "explanation": "Directories (folders) organize files hierarchically in file systems. They contain files and subdirectories, creating tree structures. Directories have metadata (name, creation date, permissions) but no data content themselves. Paths specify directory locations. Good directory organization improves file management and findability."
    },
    {
        "question": "What does PDF (Portable Document Format) do well?",
        "options": ["Looks consistent across different devices", "Plays interactive videos", "Runs programming code", "Edits music files"],
        "answer": "Looks consistent across different devices",
        "hint": "Preserves formatting across computers and printers",
        "explanation": "PDF preserves document formatting (fonts, images, layout) across different software, hardware, and operating systems. It encapsulates text, vector graphics, raster images, and interactive elements. PDF supports digital signatures, accessibility features, and print readiness. Created by Adobe, now an open ISO standard."
    },
    {
        "question": "Copy vs Cut in file operations: what's the difference?",
        "options": ["Copy duplicates, Cut moves", "Cut duplicates, Copy moves", "They do the same thing", "Copy deletes original"],
        "answer": "Copy duplicates, Cut moves",
        "hint": "Cut removes from old location, Copy leaves it there",
        "explanation": "Copy creates a duplicate in clipboard, leaving original unchanged. Cut removes original to clipboard for relocation. Both use clipboard temporary storage. Paste inserts clipboard contents. Keyboard shortcuts: Ctrl+C (Copy), Ctrl+X (Cut), Ctrl+V (Paste). Understanding these prevents accidental data loss."
    },
    {
        "question": "What is 'source code' in programming?",
        "options": ["Human-readable program instructions", "Binary machine code", "Internet connection code", "The Matrix digital rain"],
        "answer": "Human-readable program instructions",
        "hint": "What programmers write before computer translates it",
        "explanation": "Source code is human-written instructions in programming languages. It defines software functionality before compilation/interpretation into machine code. Source code is intellectual property, often protected by copyright. Open source makes code publicly available. Version control systems manage source code changes collaboratively."
    },
    {
        "question": "In programming: X=5, then X=X+1. What is X now?",
        "options": ["6 (5 + 1)", "5 (unchanged)", "4 (5 - 1)", "Error (can't add to itself)"],
        "answer": "6 (5 + 1)",
        "hint": "Variable updates its own value",
        "explanation": "This demonstrates variable reassignment. Initially X=5. The expression X+1 evaluates to 6. The assignment operator (=) stores this new value back into X, overwriting the previous value. This fundamental concept enables counters, accumulators, and state changes in programming."
    },
    {
        "question": "What does Task Manager (Ctrl+Shift+Esc) help with?",
        "options": ["Closes frozen programs", "Deletes user accounts", "Opens internet browser", "Plays computer games"],
        "answer": "Closes frozen programs",
        "hint": "Useful when applications stop responding",
        "explanation": "Task Manager displays running processes, performance metrics, startup programs, and services. It allows terminating unresponsive applications, changing process priorities, and monitoring resource usage. Access via Ctrl+Shift+Esc or Ctrl+Alt+Delete. Essential for troubleshooting performance issues and managing system resources."
    },
    {
        "question": "What does the keyboard shortcut Ctrl+S do?",
        "options": ["Saves current file/document", "Starts search function", "Stops current process", "Selects all content"],
        "answer": "Saves current file/document",
        "hint": "Save often to avoid losing work",
        "explanation": "Ctrl+S saves current document/work to storage. Regular saving prevents data loss from crashes or power outages. Most applications auto-save periodically, but manual saving ensures critical points are preserved. The save shortcut is universal across operating systems and applications, fundamental to digital work habits."
    },
    {
        "question": "Which connection is more stable for online gaming?",
        "options": ["Ethernet (wired connection)", "Wi-Fi (wireless connection)", "Bluetooth connection", "Mobile data connection"],
        "answer": "Ethernet (wired connection)",
        "hint": "Wired has less interference than wireless",
        "explanation": "Wired Ethernet provides lower latency, consistent bandwidth, and immunity to wireless interference compared to Wi-Fi. This stability is crucial for competitive gaming where milliseconds matter. Ethernet connections also offer better security and don't compete with other wireless devices. Use Cat6/Cat6a cables for best performance."
    },
    {
        "question": "What does Caps Lock do on a keyboard?",
        "options": ["Types UPPERCASE letters", "Locks computer security", "Deletes selected text", "Mutes computer sound"],
        "answer": "Types UPPERCASE letters",
        "hint": "LIKE TYPING IN ALL CAPS",
        "explanation": "Caps Lock toggles uppercase letter input without holding Shift. When active, typed letters appear capitalized while numbers/symbols remain unaffected. The key typically has an indicator light. In online communication, ALL CAPS is considered shouting. Some keyboards offer additional functions via Caps Lock key."
    },
    {
        "question": "What is a 'QR Code' (Quick Response Code)?",
        "options": ["Scannable square barcode", "Secret password code", "Computer virus code", "Broken image code"],
        "answer": "Scannable square barcode",
        "hint": "Scan with phone camera to open links or info",
        "explanation": "QR (Quick Response) codes are two-dimensional barcodes storing data in both vertical and horizontal directions. They can store URLs, contact info, Wi-Fi credentials, or other data. Smartphone cameras decode them instantly. QR codes enable contactless interactions, marketing, payments, and information sharing."
    },
    {
        "question": "What does GPS (Global Positioning System) do?",
        "options": ["Finds geographic location", "Plays video games", "Saves photo files", "Sends email messages"],
        "answer": "Finds geographic location",
        "hint": "Used for maps, navigation, tracking",
        "explanation": "GPS uses satellite constellations to determine precise geographic locations through trilateration. Receivers calculate position by timing signals from multiple satellites. GPS enables navigation, mapping, tracking, and location-based services. Modern devices combine GPS with other positioning systems (GLONASS, Galileo) for improved accuracy."
    },
    {
        "question": "What is 'Dark Mode' in apps and websites?",
        "options": ["Dark background color scheme", "Screen turned completely off", "Computer virus mode", "Broken monitor display"],
        "answer": "Dark background color scheme",
        "hint": "Easier on eyes at night, saves battery on OLED screens",
        "explanation": "Dark mode uses light text on dark backgrounds, reducing eye strain in low-light conditions and potentially saving battery on OLED displays (pixels turn off for black). It has become a standard interface option across operating systems and applications. Some users prefer it for aesthetic reasons as well."
    },
    {
        "question": "What does 'Mute' do during calls or media?",
        "options": ["Turns off sound/microphone", "Turns off screen display", "Deletes files", "Stops internet connection"],
        "answer": "Turns off sound/microphone",
        "hint": "Useful during meetings to prevent background noise",
        "explanation": "Mute temporarily disables audio output (speakers) or input (microphone) without affecting other functions. Essential for managing audio during meetings, calls, or media consumption. Hardware mute buttons provide instant control, while software mute offers more granular options. Unmuting is equally important for participation."
    },
    {
        "question": "What does 'Battery Saver' mode do?",
        "options": ["Lowers performance to save power", "Makes phone faster", "Makes screen brighter", "Automatically charges device"],
        "answer": "Lowers performance to save power",
        "hint": "Limits background activity to extend battery life",
        "explanation": "Battery saver modes extend battery life by reducing power consumption through: lowering CPU performance, decreasing screen brightness, limiting background processes, disabling non-essential features, and reducing network activity. This trade-off between performance and battery duration helps during low-charge situations."
    },
    {
        "question": "Why does restarting a computer often fix problems?",
        "options": ["Clears RAM and resets processes", "Magical computer healing", "Deletes all viruses", "Makes hardware brand new"],
        "answer": "Clears RAM and resets processes",
        "hint": "Turn off and on again - classic tech support advice",
        "explanation": "Restarting clears volatile memory (RAM), terminates all processes, reloads the operating system, and reinitializes hardware. This resolves issues caused by memory leaks, software conflicts, stuck processes, or temporary glitches. The 'reboot fix' works because it provides a clean state for system operation."
    }
]