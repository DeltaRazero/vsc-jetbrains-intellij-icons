from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/RubyIcons/icons/expui/ruby/ruby_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/RubyIcons/icons/expui/ruby/ruby.svg"),
        },
        language_ids=["ruby"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/RubyIcons/icons/expui/ruby/ruby_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/RubyIcons/icons/expui/ruby/ruby.svg"),
        },
        file_extensions=["rb"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/RubyIcons/icons/expui/erb/erbFile_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/RubyIcons/icons/expui/erb/erbFile.svg"),
        },
        file_extensions=["erb"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/RubyIcons/icons/expui/erb/rjsFile_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/RubyIcons/icons/expui/erb/rjsFile.svg"),
        },
        file_extensions=["rjs"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/RubyIcons/icons/expui/erb/rxmlFile_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/RubyIcons/icons/expui/erb/rxmlFile.svg"),
        },
        file_extensions=["rxml"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/RubyIcons/icons/expui/rake/rakeRunConfiguration_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/RubyIcons/icons/expui/rake/rakeRunConfiguration.svg"),
        },
        file_names=["rakefile"],
        file_extensions=["rakefile"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/RubyIcons/icons/expui/rake/rakeRunConfiguration_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/RubyIcons/icons/expui/rake/rakeRunConfiguration.svg"),
        },
        file_extensions=["rake"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/RubyIcons/icons/expui/ruby/rubyGems_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/RubyIcons/icons/expui/ruby/rubyGems.svg"),
        },
        file_names=["gemfile"],
    ),

    # TODO: Make custom icon with lock modifier
    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/RubyIcons/icons/expui/ruby/rubyGems_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/RubyIcons/icons/expui/ruby/rubyGems.svg"),
        },
        file_names=["gemfile.lock"],
    ),

    # TODO: todo
    icon.FolderIcon(
        (
            "/jetbrains/RubyIcons/icons/ruby/rubyModule.svg",
            "/customico/RubyIcons/icons/ruby/rubyModule-open.svg",
        ),
        ["gem", "gems", ".gem", ".gems"],
    ),

]
