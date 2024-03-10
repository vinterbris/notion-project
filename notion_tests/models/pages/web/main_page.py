import pyperclip
from selene import browser, have, be


class MainPage:

    def __init__(self):
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
        self.page_name.matching(be.present)

    def should_have_top_ui_elements(self):
        self.icon.matching(be.present)
        self.conver.matching(be.present)
        self.comments.matching(be.present)

    # TODO refactor
    def should_have_additional_top_ui_elements(self):
        self.button_open_as_full_page.matching(be.present)
        browser.element('.peekModeCenter').matching(be.present)
        browser.all('[role="button"] .notranslate').element_by(have.text('Getting Started')).matching(be.present)

    def should_have_bottom_ui_elements(self):
        self.ai.matching(be.present)
        self.import_data.matching(be.present)
        self.templates.matching(be.present)
        self.collection_table.matching(be.present)
        self.more.matching(be.present)

    class Table:

        def __init__(self):
            self.button_counter = browser.element('.typesFormula')
            self.button_add_row = browser.element('.notion-table-view-add-row')
            self.button_add_new_item = browser.element('.notion-collection-view-item-add')
            self.edit_layout = browser.element('.notion-collection-edit-view')
            self.search = browser.element('.collectionSearch')
            self.automations = browser.element('.notion-collection-automation-edit-view')
            self.button_count = browser.all('[role="button"]').element_by(have.text('Count'))
            self.button_sort = browser.all('[role="button"]').element_by(have.text('Sort'))
            self.button_filter = browser.all('[role="button"]').element_by(have.text('Filter'))
            self.buttons_all_new = browser.all('.plus')
            self.tabs = browser.all('.notion-collection-view-tab-button')
            self.table_view = browser.element('.notion-table-view')

        def should_have_table_view(self):
            self.table_view.matching(be.present)

        def should_have_tabs(self, tab1, tab2):
            self.tabs.should(have.texts(tab1, tab2))

        def should_have_buttons_new(self, value):
            self.buttons_all_new.should(have.size(value))

        def should_have_buttons(self):
            self.button_filter.matching(be.present)
            self.button_sort.matching(be.present)
            self.button_count.matching(be.present)

        def should_have_ui_elements(self):
            self.automations.matching(be.present)
            self.search.matching(be.present)
            self.edit_layout.matching(be.present)
            self.button_add_new_item.matching(be.present)
            self.button_add_row.matching(be.present)
            self.button_counter.matching(be.present)

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
            self.favorites_header.matching(be.absent)
            self.favorites_block.matching(be.absent)

        def open_page_options_panel(self):
            self.button_page_options.click()

        def should_have_topbar_ui_elements(self):
            self.share_menu.matching(be.present)
            self.button_comments.matching(be.present)
            self.button_updates.matching(be.present)
            self.button_favorites.matching(be.present)
            self.button_page_options.matching(be.present)

    class SideBar:
        def __init__(self):
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
            browser.element('.notion-outliner-private .notion-page-block').hover()
            browser.element('.notion-outliner-private .notion-page-block .plusThick').click()

        def choose_last_page(self):
            self.last_page.click()

        def should_have_sidebar_ui_elements(self):
            browser.element('.notion-sidebar-switcher').should(have.text("Sergey's Notion"))
            browser.element('.notion-close-sidebar').matching(be.present)
            browser.element('.sidebarSearch').matching(be.present)
            browser.element('.sidebarInbox').matching(be.present)
            browser.element('.sidebarSettings').matching(be.present)
            browser.element('.circlePlus').matching(be.present)
            browser.element('.notion-outliner-private').matching(be.present)
            browser.element('.plusThick').matching(be.present)
            browser.element('.calendarDate09').matching(be.present)
            browser.element('.typesRelation').matching(be.present)
            browser.element('.sidebarInviteTeam').matching(be.present)
            browser.element('.sidebarImport').matching(be.present)
            browser.element('.trash').matching(be.present)

        def should_have_title(self, value):
            self.collection_of_pages.element_by(have.text(value)).matching(be.present)

        def favorites_should_have_page_with_name(self, value):
            self.bookmarks.should(have.text(value))
            
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
            self.button_publish.matching(be.present)
            self.button_publish.press_escape()

    class PageOptionsMenu:
        def __init__(self, sidebar):
            self.sidebar = sidebar
            self.menu_delete = browser.all('[role="menuitem"]').element_by(have.text('Delete'))

        def choose_delete(self):
            self.menu_delete.click()
            self.sidebar.list_of_pages.wait_until(have.size(1))

    class TemplatesWindow:
        def __init__(self):
            self.button_get_template = browser.all('[role="button"]').element_by(have.text('Get template'))
            self.todo_list = browser.element('#tg-simple_tasks')

        def choose_todo_list(self):
            self.todo_list.click()

        def get_template(self):
            self.button_get_template.click()
