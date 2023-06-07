#!/usr/local/bin/lua

function main ()
    if #arg == 0 then
        open_files()
        arturia_mappings()
    elseif #arg == 1 then
        if arg[1] == "-t" then
            print("test succesful")
        else
            print("invalid arg.")
        end
    else
        print("too many args you schmuck")

    end
end

function open_files()
    os.execute("open ~/Music/Ableton/the_carnival_project/the_carnival.als")
    os.execute("open -a Amphetamine.app")
end

function arturia_mappings () 
    mappings = [[Arturia Minilab Mappings for this project 
Play Button: Drumpad 1 
Pause Button: Drumpad 2]]
    print(mappings)
end

main()
