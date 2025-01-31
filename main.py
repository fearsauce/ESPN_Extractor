""" Run ESPN Fantasy Data Extractor """
from espn_extractor.league_history import extract_team_records
from espn_extractor.draft_board import extract_draft_board, extract_draft_positions
from espn_extractor.draft_board_excel import extract_draft_cheatsheet
import config

if __name__ == '__main__':
    extract_team_records(config, False)
    extract_draft_board(config, False)
    extract_draft_positions(config, False)
    extract_draft_cheatsheet(config, False)
