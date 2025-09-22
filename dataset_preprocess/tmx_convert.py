import xml.etree.ElementTree as ET

def fast_tmx_to_txt(tmx_file, txt_file):
    with open(txt_file, 'w', encoding='utf-8') as out_file:
        for event, elem in ET.iterparse(tmx_file, events=('end',)):
            if elem.tag == 'tu':
                try:
                    src, tgt = None, None
                    for tuv in elem.findall('tuv'):
                        lang = tuv.attrib.get('{http://www.w3.org/XML/1998/namespace}lang')
                        seg = tuv.find('seg')
                        if lang == 'en':
                            src = seg.text if seg is not None else None
                        elif lang == 'fr':
                            tgt = seg.text if seg is not None else None
                    if src and tgt:
                        out_file.write(f"{src}\t{tgt}\n")
                except Exception as e:
                    pass
                elem.clear()  # Free memory



def tmx_to_tsv(tmx_file, tsv_file):
    """
    Convert a TMX file to a TSV file with source-target pairs (tab-separated).
    
    Args:
    - tmx_file (str): Path to the input TMX file.
    - tsv_file (str): Path to the output TSV file.
    """
    # Parse the TMX XML file
    tree = ET.parse(tmx_file)
    root = tree.getroot()

    with open(tsv_file, 'w', encoding='utf-8') as out_file:
        # Iterate through each <tu> (Translation Unit) in the TMX file
        for tu in root.findall(".//tu"):
            # Get the source and target text from <tuv> elements
            source = tu.find(".//tuv[@xml:lang='en']/seg")
            target = tu.find(".//tuv[@xml:lang='fr']/seg")

            if source is not None and target is not None:
                # Write source and target text to the output file, tab-separated
                out_file.write(f"{source.text}\t{target.text}\n")

if __name__ == "__main__":
    # Example usage
    tmx_file = 'pre-process_dataset\en-fr.roam.tmx'   # Path to your TMX file
    txt_file = 'crawl.txt'      # Output TXT file

    # Choose the conversion function
    fast_tmx_to_txt(tmx_file, txt_file)  # Converts to plain TXT
    # Or use:
    # tmx_to_tsv(tmx_file, tsv_file)  # Converts to TSV
