# PowerShell script to rename PDF files to "This Kind Of Style" format

# Function to convert filename to Title Case
function Convert-ToTitleCase($name) {
    $name = $name -replace '\.pdf$', ''
    $name = $name -replace '_', ' '
    $name = $name -replace '-', ' '
    $name = $name.ToLower()
    $name = (Get-Culture).TextInfo.ToTitleCase($name)
    return "$name.pdf"
}

# AutoML directory
$autoMLFiles = @{
    'AFE_master.pdf' = 'AFE Master.pdf'
    'AIDE.pdf' = 'AIDE Framework.pdf'
    'AgentLaboratory.pdf' = 'Agent Laboratory.pdf'
    'AutoKaggle.pdf' = 'AutoKaggle Platform.pdf'
    'AutoML-Agent.pdf' = 'AutoML Agent.pdf'
    'DATA INTERPRETER.pdf' = 'Data Interpreter.pdf'
    'DOLPHIN.pdf' = 'DOLPHIN System.pdf'
    'DS-Agent.pdf' = 'DS Agent.pdf'
    'I-MCTS.pdf' = 'I MCTS Algorithm.pdf'
    'LightAutoDS-Tab.pdf' = 'LightAutoDS Tab.pdf'
    'ML-Agent.pdf' = 'ML Agent.pdf'
    'ML-Master.pdf' = 'ML Master.pdf'
    'MLZero.pdf' = 'ML Zero.pdf'
    'OpenHands.pdf' = 'OpenHands Platform.pdf'
    'Paper2Code.pdf' = 'Paper2Code.pdf'
    'R&D-Agent.pdf' = 'R&D Agent.pdf'
    'TabPFN.pdf' = 'TabPFN Model.pdf'
    'caafe.pdf' = 'CAAFE Framework.pdf'
    'huawei-agent K1.pdf' = 'Huawei Agent K1.pdf'
    'llmfe.pdf' = 'LLM Feature Engineering.pdf'
    'ocTree.pdf' = 'OCTree Algorithm.pdf'
    'openFE.pdf' = 'OpenFE Framework.pdf'
    'real-TabPFN.pdf' = 'Real TabPFN.pdf'
    'sela.pdf' = 'SELA Framework.pdf'
}

# AI4Science directory
$ai4ScienceFiles = @{
    '41467_2024_48779_MOESM1_ESM.pdf' = 'Mathematical Discoveries From Program Search.pdf'
    'Data-driven energy management for electric.pdf' = 'Data Driven Energy Management For Electric.pdf'
    'PINN-SOH.pdf' = 'PINN SOH Framework.pdf'
}

# LLM4CO directory
$llm4coFiles = @{
    'Romera-Paredes 等 - 2023 - Mathematical discoveries from program search with .pdf' = 'Mathematical Discoveries From Program Search.pdf'
    'Sun 等 - 2025 - CO-Bench Benchmarking Language Model Agents in Al.pdf' = 'CO Bench Benchmarking Language Model Agents.pdf'
    'Ye 等 - 2024 - ReEvo Large Language Models as Hyper-Heuristics w.pdf' = 'ReEvo Large Language Models As Hyper Heuristics.pdf'
}

# Security directory
$securityFiles = @{
    '1. Fundamentals of AI.pdf' = 'Fundamentals Of AI.pdf'
    '2. Applications of AI in InfoSec.pdf' = 'Applications Of AI In InfoSec.pdf'
    '3. Introduction to Red Teaming AI.pdf' = 'Introduction To Red Teaming AI.pdf'
    '4. Prompt Injection Attacks.pdf' = 'Prompt Injection Attacks.pdf'
}

# Surveys directory
$surveysFiles = @{
    'A Survey on Large Language Model-based.pdf' = 'Large Language Model Based Survey.pdf'
    'A-General-Survey-on-Attention-Mechanisms-in-DeepLearing.pdf' = 'Attention Mechanisms In Deep Learning Survey.pdf'
    'ADVANCES-AND-CHALLENGES-IN-FOUNDATION-AGENTS.pdf' = 'Advances And Challenges In Foundation Agents.pdf'
    'Data Analysis in the Era of Generative AI.pdf' = 'Data Analysis In The Era Of Generative AI.pdf'
    'Large Language Models for Data Science A Survey.pdf' = 'Large Language Models For Data Science Survey.pdf'
    'Large-Language-Model-Agent-A-Survey-on.pdf' = 'Large Language Model Agent Survey.pdf'
    'Measuring Data Science Automation.pdf' = 'Measuring Data Science Automation.pdf'
    'llm4ml-workflows-survey.pdf' = 'LLM4ML Workflows Survey.pdf'
    'survey of EDA.pdf' = 'Survey Of EDA.pdf'
    'survey_embodied_ai.pdf' = 'Embodied AI Survey.pdf'
}

# Benchmark directory
$benchmarkFiles = @{
    'DataSciBench.pdf' = 'DataSciBench.pdf'
    'IDA-bench.pdf' = 'IDA Bench.pdf'
    'MLE-bench.pdf' = 'MLE Bench.pdf'
}

# Function to rename files
function Rename-Files($directory, $fileMapping) {
    foreach ($oldName in $fileMapping.Keys) {
        $newName = $fileMapping[$oldName]
        $oldPath = Join-Path $directory $oldName
        $newPath = Join-Path $directory $newName
        
        if (Test-Path $oldPath) {
            Rename-Item -Path $oldPath -NewName $newName -Force
            Write-Host "Renamed: $oldName -> $newName"
        } else {
            Write-Host "File not found: $oldName"
        }
    }
}

# Execute renaming
Write-Host "Starting file renaming..."

Rename-Files 'AutoML' $autoMLFiles
Rename-Files 'AI4Science' $ai4ScienceFiles
Rename-Files 'LLM4CO' $llm4coFiles
Rename-Files 'Security' $securityFiles
Rename-Files 'Surveys' $surveysFiles
Rename-Files 'benchmark' $benchmarkFiles

Write-Host "File renaming completed!"