from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        "/customico/RubyIcons/icons/ruby/rubyFile-fixed.svg",
        file_extensions=["rb"],
    ),

    icon.FileIcon(
        "/jetbrains/RubyIcons/icons/erb/erbFile.svg",
        file_extensions=["erb"],
    ),

    icon.FileIcon(
        "/jetbrains/RubyIcons/icons/erb/rjsFile.svg",
        file_extensions=["rjs"],
    ),

    icon.FileIcon(
        "/jetbrains/RubyIcons/icons/erb/rxmlFile.svg",
        file_extensions=["rxml"],
    ),

    icon.FileIcon(
        "/jetbrains/RubyIcons/icons/rake/rake_runConfiguration.svg",
        file_names=["rakefile"],
        file_extensions=["rakefile"],
    ),

    icon.FileIcon(
        "/jetbrains/RubyIcons/icons/rake/rakeTaskDescription.svg",
        file_extensions=["rake"],
    ),

    icon.FileIcon(
        "/jetbrains/RubyIcons/icons/ruby/ruby.svg",
        file_names=["gemfile"],
    ),

    # TODO: Make custom icon with lock modifier
    icon.FileIcon(
        "/jetbrains/RubyIcons/icons/ruby/ruby.svg",
        file_names=["gemfile.lock"],
    ),

    icon.FolderIcon(
        (
            "/jetbrains/RubyIcons/icons/ruby/rubyModule.svg",
            "/customico/RubyIcons/icons/ruby/rubyModule-open.svg",
        ),
        ["gem", "gems", ".gem", ".gems"],
    ),

]
