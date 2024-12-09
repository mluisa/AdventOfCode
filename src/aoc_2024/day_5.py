import re
from collections import defaultdict

from src.aoc_2024.helpers import file_reader


class Day5:
    def __init__(self, filename: str):
        self.puzzle = file_reader.get_lines(filename)
        self.middle_index = self.puzzle.index("")
        self.pages_order = self._get_ordering_rules()
        self.pages_to_produce = self._get_pages_to_produce()

    def part_1(self):
        correct_ordered_pages = []
        middle_pages = []
        for pages_to_produce in self.pages_to_produce:
            for i in range(len(pages_to_produce) - 1):
                if pages_to_produce[i + 1] not in self.pages_order[pages_to_produce[i]]:
                    break

                if i == len(pages_to_produce) - 2:
                    correct_ordered_pages.append(pages_to_produce)
                    middle_pages.append(pages_to_produce[len(pages_to_produce) // 2])

        return sum([int(page) for page in middle_pages])

    def part_2(self):
        incorrect_ordered_pages = []
        middle_pages = []
        for pages_to_produce in self.pages_to_produce:
            for i in range(len(pages_to_produce) - 1):
                if pages_to_produce[i + 1] not in self.pages_order[pages_to_produce[i]]:
                    incorrect_ordered_pages.append(pages_to_produce)
                    break

            fixed_ordered_pages = []
            for incorrect_page_order in incorrect_ordered_pages:
                ordered_pages = self._fix_pages_ordering(incorrect_page_order)
                fixed_ordered_pages.append(ordered_pages)

        for fixed_ordered_page in fixed_ordered_pages:
            middle_pages.append(fixed_ordered_page[len(fixed_ordered_page) // 2])

        return sum([int(page) for page in middle_pages])

    def _fix_pages_ordering(self, incorrect_page_order):
        # Order the incorrect pages order
        ordered_pages = incorrect_page_order[:]
        max_attempts = 1000
        attempts = 0

        while attempts < max_attempts:
            attempts += 1
            new_order = ordered_pages[:]

            for i in range(len(ordered_pages) - 1):
                current_page = ordered_pages[i]
                next_page = ordered_pages[i + 1] if len(ordered_pages) > i + 1 else None

                if next_page not in self.pages_order[current_page]:
                    if current_page in self.pages_order[next_page]:
                        # Swap the pages
                        new_order[i], new_order[i + 1] = ordered_pages[i + 1], ordered_pages[i]
                    else:
                        # Ensure we provide a default value for `next()` to avoid StopIteration
                        next_correct_page = next(
                            (page for page in self.pages_order[current_page] if page in ordered_pages),
                            None  # Default value
                        )

                        if next_correct_page is None:
                            # If no valid next page was found, handle the error or break the loop
                            continue  # Skip this iteration

                        # Proceed with the logic only if next_correct_page is not None
                        next_page_index = ordered_pages.index(next_correct_page)
                        new_order[i + 1], new_order[next_page_index] = ordered_pages[next_page_index], ordered_pages[
                            i + 1]

                else:
                    if i == 0:
                        new_order[i] = current_page
                    new_order[i + 1] = next_page

            # If no change was made, we can break out of the loop
            if new_order == ordered_pages:
                break

            ordered_pages = new_order

        # After the loop ends, we check if the order is correct
        if self._is_correctly_ordered(ordered_pages):
            return ordered_pages
        else:
            return ordered_pages

    def _is_correctly_ordered(self, ordered_pages):
        for i in range(len(ordered_pages) - 1):
            if ordered_pages[i + 1] not in self.pages_order[ordered_pages[i]]:
                break

            if i == len(ordered_pages) - 2:
                return True
        return False

    def _get_ordering_rules(self):
        ordering_rules = [rule.split("|") for rule in self.puzzle[:self.middle_index]]
        pages_orders = defaultdict(list)
        for rule in ordering_rules:
            pages_orders[int(rule[0])].append(int(rule[1]))

        for key in pages_orders:
            pages_orders[key].sort()

        return pages_orders

    def _get_pages_to_produce(self):
        updates = self.puzzle[self.middle_index + 1:]
        pages_to_produce = []
        for update in updates:
            pages_to_produce.append([int(x) for x in update.split(",")])

        return pages_to_produce


def main():
    day_5 = Day5(filename="day_5.txt")

    print('Advent of Code 2024 : Day 5')
    print('===========================')
    print('Part 1')
    print(f"Sum of middle page: {day_5.part_1()}")
    print('Part 2')
    print(f"Sum of middle page: {day_5.part_2()}")


if __name__ == "__main__":
    main()