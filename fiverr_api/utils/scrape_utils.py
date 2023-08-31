def extract_text(element, class_name=None):
    if element:
        if class_name:
            found_element = element.find(class_=class_name)
            return found_element.text if found_element else None
        return element.text
    return None


def extract_list_items(element, class_name=None):
    if element:
        if class_name:
            return [item.text for item in element.find_all(class_=class_name)]
        return [item.text for item in element.find_all('li')]
    return []
