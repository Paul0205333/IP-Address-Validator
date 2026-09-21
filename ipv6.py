import re
regex = r"^(?:(?:[a-fA-F0-9]{1,4}):){7}[a-fA-F0-9]{1,4}$"

def is_valid_ipv6(input):
    if "::" in input:
        if input.count("::") > 1:
            return "The IP Address: {ip} is invalid".format(ip=input)

        left, right = input.split("::")

        left_groups = left.split(":") if left else []
        right_groups = right.split(":") if right else []
        middle_groups = []

        if len(left_groups) + len(right_groups) > 8:
            return "The IP Address: {ip} is invalid".format(ip=input)

        insert_times = 8 - (len(left_groups) + len(right_groups))

        middle_groups += ["0000"] * insert_times

        combined = transform_to_expanded(left_groups) + middle_groups + transform_to_expanded(right_groups)
        expanded_ipv6 = ":".join(combined)

        return f"""
        The IP Address: {input} is valid.
        Compressed: {input.lower()}
        Expanded: {expanded_ipv6}
        """
    elif re.match(regex, input):
        return "The IP Address: {ip} is valid".format(ip=input)
    return "The IP Address: {ip} is invalid".format(ip=input)

def transform_to_expanded(ip_list):
    return [ip.lower().zfill(4) for ip in ip_list]