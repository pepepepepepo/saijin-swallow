<img width="2065" height="1304" alt="mermaid-diagram-2025-10-01-143540" src="https://github.com/user-attachments/assets/6e7a857f-4f24-4207-ade9-d968cf7e5756" />

flowchart LR
    subgraph OnPrem[On-Prem（社内ネットワーク）]
        AD[Active Directory] -- TCP 389 --> Core[Kimirano-Core（管理サーバー）]
        Domino[Domino Server] -- TCP 1352 --> Core
        Client[Client Devices] -- TCP 139/445 & 443 --> Core
        Core -- TCP 1433 --> DB[(Kimirano-DB)]
    end
    subgraph Cloud[Cloud Environment]
        ExO[Exchange Online]
        Ex[Exchange Server]
    end
    Core -- TCP 443 --> ExO
    Core -- TCP 443 --> Ex
    Core -- TCP 80 & 443 --> Ex
