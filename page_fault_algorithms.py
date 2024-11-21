def first_in_first_out(reference_string, frame_size):
    frame = []
    page_faults = 0
    print(f"The refference string given is {reference_string}")
    print(f"The frame size given in {frame_size}")
    for page in reference_string:
        if(page in frame):
            print(f"Page {page} did not cause any fault : {frame}")
            continue
        else:
            if len(frame) < frame_size:
                frame.append(page)
            else:
                frame.pop(0)
                frame.append(page)
            page_faults += 1
            print(f"Page {page} caused a fault : {frame}")
    print(f"Final Frame after all the page fault : {frame}")
    print(f"Total Number of page faults : {page_faults}")



def least_recently_used(reference_string , frame_size):
    frame = []
    page_faults = 0
    page_usage = {}
    print(f"The given refernce string is : {reference_string}")
    print(f"The given frame size is : {frame_size}")

    for i ,page in enumerate(reference_string):
        if page in frame:
            print(f"The page {page} did not cause any fault : {frame}")
        else:
            page_faults += 1
            if len(frame) < frame_size:
                frame.append(page)
            else:
                lru_page = min(page_usage , key=page_usage.get)
                frame.remove(lru_page)
                del page_usage[lru_page]
                frame.append(page)
            print(f"The page {page} caused page fault : {frame}")
        page_usage[page] = i
    print(f"Total Number of page faults : {page_faults}")


def optimal_page_replacement(reference_string , frame_size):
    frame = []
    page_fault = 0

    print(f"Reference String : {reference_string}")
    print(f"Frame size : {frame_size}")

    for i , page in enumerate(reference_string):
        if page in frame:
            print(f"Page {page} did not cause any page fault : {frame}")
        else:
            page_fault += 1 
            if len(frame) < frame_size:
                frame.append(page)
            else:
                farthest_index = -1
                page_to_replace = None

                for current_page in frame:
                    if current_page not in reference_string[i+1:]:
                        page_to_replace = current_page
                        break
                    else:
                        future_index = reference_string[i+1:].index(current_page)
                        if farthest_index < future_index:
                            farthest_index = future_index
                            page_to_replace = current_page
                frame[frame.index(page_to_replace)] = page
            print(f"Page {page} cause a page fault : {frame}")
                
    print(f"The page fault is : {page_fault}")

reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_size = 3  # Number of available frames in memory

# Run the function
optimal_page_replacement(reference_string, frame_size)

