import time

import pyperclip
from selene import browser, have, be


class MainPage:

    def __init__(self):
        self.button_choose_default_page_getting_started = browser.all('[role="button"] .notranslate').element_by(
            have.text('Getting Started'))
        self.button_choose_peek_mode = browser.element('.peekModeCenter')
        self.subpage_name = browser.element('.notion-overlay-container [placeholder="Untitled"]')
        self.button_open_as_full_page = browser.element('.openAsPageThick')
        self.more = browser.element('.notion-page-content .dots')
        self.collection_table = browser.element('.collectionTable')
        self.templates = browser.element('.templates')
        self.import_data = browser.element('.import')
        self.ai = browser.element('.sparkles')
        self.comments = browser.element('.addPageDiscussion')
        self.conver = browser.element('.addPageCover')
        self.icon = browser.element('.addPage')
        self.templates_window = self.TemplatesWindow()
        self.page_name = browser.element('[placeholder="Untitled"]')

        self.sidebar = self.SideBar()
        self.topbar = self.TopBar()
        self.share_menu = self.ShareMenu()
        self.page_options = self.PageOptionsMenu(self.sidebar)
        self.table = self.Table()

    def enter_page_name(self, name):
        self.page_name.click().type(name)

    def enter_subpage_name(self, name):
        self.subpage_name.click().type(name)

    def open_in_full_page(self):
        self.button_open_as_full_page.click()

    def should_have_title_field(self):
        self.page_name.should(be.present)

    def should_have_top_ui_elements(self):
        self.icon.should(be.present)
        self.conver.should(be.present)
        self.comments.should(be.present)

    def should_have_additional_top_ui_elements(self):
        self.button_open_as_full_page.should(be.present)
        self.button_choose_peek_mode.should(be.present)
        self.button_choose_default_page_getting_started.should(be.present)

    def should_have_bottom_ui_elements(self):
        self.ai.should(be.present)
        self.import_data.should(be.present)
        self.templates.should(be.present)
        self.collection_table.should(be.present)
        self.more.should(be.present)

    class Table:

        def __init__(self):
            self.button_counter = browser.element('.typesFormula')
            self.button_add_row = browser.element('.notion-table-view-add-row')
            self.button_add_new_item = browser.element('.notion-collection-view-item-add')
            self.edit_layout = browser.element('.notion-collection-edit-view')
            self.search = browser.element('.collectionSearch')
            self.automations = browser.element('.notion-collection-automation-edit-view')
            self.button_sort = browser.all('[role="button"]').element_by(have.text('Sort'))
            self.button_filter = browser.all('[role="button"]').element_by(have.text('Filter'))
            self.buttons_all_new = browser.all('.plus')
            self.tabs = browser.all('.notion-collection-view-tab-button')
            self.table_view = browser.element('.notion-table-view')

        def should_have_table_view(self):
            self.table_view.should(be.present)

        def should_have_tabs(self, tab1, tab2):
            self.tabs.should(have.texts(tab1, tab2))

        def should_have_buttons_new(self, value):
            self.buttons_all_new.should(have.size(value))

        def should_have_buttons(self):
            self.button_filter.should(be.present)
            self.button_sort.should(be.present)

        def should_have_ui_elements(self):
            self.automations.should(be.present)
            self.search.should(be.present)
            self.edit_layout.should(be.present)
            self.button_add_new_item.should(be.present)
            self.button_add_row.should(be.present)
            self.button_counter.should(be.present)

    class TopBar:

        def __init__(self):
            self.button_favorites = browser.element('.notion-topbar-favorite-button')
            self.button_updates = browser.element('.notion-topbar-updates-button')
            self.button_comments = browser.element('.notion-topbar-comments-button')
            self.share_menu = browser.element('.notion-topbar-share-menu')
            self.button_add_to_favorites = browser.element('.topbarStar')
            self.indicator_added_to_favorite = browser.element('.topbarStarFilled')
            self.favorites_block = browser.element('.notion-outliner-bookmarks')
            self.favorites_header = browser.element('.notion-outliner-bookmarks-header-container')
            self.button_page_options = browser.element('.notion-topbar-more-button')

        def add_page_to_favorites(self):
            self.button_add_to_favorites.click()

        def unfavorite_page(self):
            self.indicator_added_to_favorite.click()
            self.favorites_header.should(be.absent)
            self.favorites_block.should(be.absent)

        def open_page_options_panel(self):
            self.button_page_options.click()

        def should_have_topbar_ui_elements(self):
            self.share_menu.should(be.present)
            self.button_comments.should(be.present)
            self.button_updates.should(be.present)
            self.button_favorites.should(be.present)
            self.button_page_options.should(be.present)

    class SideBar:
        def __init__(self):
            self.button_archive_without_moving_pages = browser.all('[role="button"]').element_by(
                have.text('Proceed without moving pages'))
            self.button_archive_teamspace = browser.all('[role="button"]').element_by(have.text('Archive teamspace'))
            self.menu_archive_teamspace = browser.all('[role="menuitem"]').element_by(have.text('Archive teamspace'))
            self.teamspace_home = browser.all('.notion-outliner-team').element_by(have.text('Teamspace Home'))
            self.list_of_teamspace_pages = browser.all('.notion-outliner-team')
            self.teamspace_page = browser.element('.notion-outliner-team')
            self.button_teamspace_page_plus = browser.element('.notion-outliner-team-header-container .plusThick')
            self.list_of_buttons = browser.all('[role="button"]')
            self.teamspace_header_container = browser.element('.notion-outliner-team-header-container')
            self.button_trash = browser.element('.trash')
            self.button_import = browser.element('.sidebarImport')
            self.button_calendar = browser.all('[role="button"]').element_by(have.text('Calendar'))
            self.block_of_private_pages = browser.element('.notion-outliner-private')
            self.button_new_page = browser.element('.circlePlus')
            self.settings = browser.element('.sidebarSettings')
            self.inbox = browser.element('.sidebarInbox')
            self.search = browser.element('.sidebarSearch')
            self.button_close_sidebar = browser.element('.notion-close-sidebar')
            self.sidebar_switcher = browser.element('.notion-sidebar-switcher')
            self.button_skip_people_invite = browser.all('[role="button"]').element_by(have.text('Skip for now'))
            self.button_submit_teamspace = browser.all('[role="button"]').element_by(have.text('Create teamspace'))
            self.teamspace_name = browser.element('[placeholder="Acme Labs"]')
            self.button_create_teamspace = browser.all('[role="button"]').element_by(have.text('Create a teamspace'))
            self.page_button_plus = browser.element('.notion-outliner-private .notion-page-block .plusThick')
            self.page = browser.element('.notion-outliner-private .notion-page-block')
            self.bookmarks = browser.element('.notion-outliner-bookmarks')
            self.collection_of_pages = browser.all('.notranslate')
            self.button_templates = browser.element('.sidebarTemplates')
            self.button_add_page = browser.all('[role="button"]').element_by(have.text('Add a page'))
            self.last_page = browser.all('[role="treeitem"]')[-1]
            self.list_of_pages = browser.all('.notion-outliner-private .notion-selectable')

        def open_templates(self):
            self.button_templates.click()

        def add_page(self):
            self.button_add_page.click()

        def add_subpage(self):
            self.page.hover()
            self.page_button_plus.click()

        def choose_last_page(self):
            self.last_page.click()

        def create_teamspace(self):
            self.button_create_teamspace.click()

        def name_teamspace(self, workspace_name):
            self.teamspace_name.type(workspace_name)

        def submit_teamspace(self):
            self.button_submit_teamspace.click()

        def skip_people_invite(self):
            self.button_skip_people_invite.click()

        def should_have_sidebar_ui_elements(self, value):
            self.sidebar_switcher.should(have.text(value))
            self.button_close_sidebar.should(be.present)
            self.search.should(be.present)
            self.inbox.should(be.present)
            self.settings.should(be.present)
            self.button_new_page.should(be.present)
            self.block_of_private_pages.should(be.present)
            self.button_add_page.should(be.present)
            self.button_calendar.should(be.present)
            self.button_create_teamspace.should(be.present)
            self.button_import.should(be.present)
            self.button_trash.should(be.present)

        def should_have_teamspace_ui_elemnts(self, workspace_name):
            self.teamspace_header_container.should(be.present)
            self.list_of_buttons.element_by(have.text(workspace_name)).should(be.present)
            self.button_teamspace_page_plus.should(be.present)
            self.teamspace_page.should(be.present)
            self.list_of_teamspace_pages.element_by(have.text(workspace_name)).should(be.present)
            self.teamspace_home.should(be.present)

        def should_have_title(self, value):
            self.collection_of_pages.element_by(have.text(value)).should(be.present)

        def favorites_should_have_page_with_name(self, value):
            self.bookmarks.should(have.text(value))

        def archive_teamspace(self, workspace_name):
            self.list_of_teamspace_pages.element_by(have.text(workspace_name)).hover()
            self.list_of_teamspace_pages.element_by(have.text(workspace_name)).element('.dots').click()
            self.menu_archive_teamspace.click()
            browser.element(f'[placeholder="{workspace_name}"]').type(workspace_name)
            self.button_archive_teamspace.click()
            self.button_archive_without_moving_pages.click()
            self.teamspace_header_container.should(be.absent)

    class ShareMenu:

        def __init__(self):
            self.view_site_button = browser.element('.globe2')
            self.link = browser.element('.link')
            self.button_publish = browser.element('.notion-share-menu-publish-button')
            self.share_menu_publish_tab = browser.element('.notion-share-menu-publish-tab')
            self.button_share_menu = browser.element('.notion-topbar-share-menu')
            self.button_unpublish = browser.all('[role="button"]').element_by(have.text('Unpublish'))

        def open_share_menu(self):
            self.button_share_menu.click()

        def open_publish_tab(self):
            self.share_menu_publish_tab.click()

        def publish_page(self):
            self.button_publish.click()

        def get_link(self):
            self.link.click()
            self.view_site_button.wait_until(be.visible)
            return pyperclip.paste()

        def unpublish_page(self):
            self.button_unpublish.click()
            self.button_publish.should(be.present)
            self.button_publish.press_escape()

    class PageOptionsMenu:
        def __init__(self, sidebar):
            self.sidebar = sidebar
            self.menu_delete = browser.all('[role="menuitem"]').element_by(have.text('Delete'))

        def choose_delete(self):
            self.menu_delete.click()
            self.sidebar.list_of_pages.wait_until(have.size(1))
            time.sleep(2)

    class TemplatesWindow:
        def __init__(self):
            self.button_get_template = browser.all('[role="button"]').element_by(have.text('Get template'))
            self.todo_list = browser.element('#tg-simple_tasks')

        def choose_todo_list(self):
            self.todo_list.click()

        def get_template(self):
            self.button_get_template.click()
