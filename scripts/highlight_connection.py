import os
import xml.etree.ElementTree as ET

# File paths
network_file = r"C:\Users\Kartikeya A Yadav\Desktop\Traffic-RL-Project\environment\intersection.net.xml"
route_file = r"C:\Users\Kartikeya A Yadav\Desktop\Traffic-RL-Project\environment\traffic.rou.xml"

# Load XML files
network_tree = ET.parse(network_file)
network_root = network_tree.getroot()
route_tree = ET.parse(route_file)
route_root = route_tree.getroot()


def find_and_fix_broken_connections():
    # Read all routes from the route file
    routes = route_root.findall(".//route")
    total_broken = 0

    # For each route, highlight and fix connections in the network file
    for route in routes:
        route_id = route.get("id")
        edges = route.get("edges").split()
        print(f"\nChecking connections for route {route_id}: {edges}")

        for i in range(len(edges) - 1):
            start_edge = edges[i]
            end_edge = edges[i + 1]
            connection_found = False

            # Search for the connection in the network file
            for connection in network_root.findall(".//connection"):
                if connection.get("from") == start_edge and connection.get("to") == end_edge:
                    connection_found = True
                    break

            if not connection_found:
                total_broken += 1
                print(f"Broken connection detected: {start_edge} -> {end_edge}")
                add_missing_connection(start_edge, end_edge)

    # Save the fixed network file
    if total_broken > 0:
        network_tree.write("fixed_intersection.net.xml", encoding="utf-8", xml_declaration=True)
        print(f"\nFixed {total_broken} broken connections.")
        print("✅ Fixed network file saved as 'fixed_intersection.net.xml'.")
    else:
        print("\nNo broken connections detected. Network file is clean.")


def add_missing_connection(start_edge, end_edge):
    # Add a missing connection with default attributes
    print(f"Adding missing connection: {start_edge} -> {end_edge}")
    new_connection = ET.Element("connection")
    new_connection.set("from", start_edge)
    new_connection.set("to", end_edge)
    new_connection.set("fromLane", "0")
    new_connection.set("toLane", "0")
    new_connection.set("dir", "s")  # Default: straight direction
    new_connection.set("state", "M")  # Default: standard connection

    # Find the <connections> section, or create it if missing
    connections_section = network_root.find(".//connections")
    if connections_section is None:
        connections_section = ET.SubElement(network_root, "connections")

    connections_section.append(new_connection)


# Run the script
find_and_fix_broken_connections()
