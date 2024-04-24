import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.JobAddlInfoSvc
// Description: 
// Version: v1



//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => application/json
   */  
export function getServiceDocument(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<JSON>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAddlInfoSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as JSON)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: Returns metadata document => content
   */  
export function get_metadata(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAddlInfoSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method Overrides
   OperationID: Overrides
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Overrides_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Overrides(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAddlInfoSvc/Overrides", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetJobInfo
   Description: Returns Job Add Info details
   OperationID: GetJobInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJobInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJobInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetJobInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAddlInfoSvc/GetJobInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOperations
   Description: Returns Operations data set
   OperationID: GetOperations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOperations_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOperations(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAddlInfoSvc/GetOperations", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetResourceGroups
   Description: Returns Resource Groups data set
   OperationID: GetResourceGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetResourceGroups_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetResourceGroups(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAddlInfoSvc/GetResourceGroups", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Erp_Tablesets_JobAddInfoDtlRow{
   ProdCrewSize:number,
   SetUpCrewSize:number,
   OpDtlSeq:number,
   OprSeq:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobAddlInfoRow{
   PartNum:string,
   PartDescription:string,
   ProdQty:number,
   DrawNum:string,
   RevisionNum:string,
   StartDate:string,
   DueDate:string,
   AsmPartNum:string,
   AsmDescription:string,
   AsmRequiredQty:number,
   AsmDrawNum:string,
   AsmRevisionNum:string,
   AsmStartDate:string,
   AsmDueDate:string,
   OprOPDesc:string,
   OprRunQty:number,
   OprQtyLeft:number,
   OprSetupLeft:number,
   OprEstSetHours:number,
   OprSetupCrewSize:number,
   OprProdStandard:number,
   OprStdFormat:string,
   OprStdBasis:string,
   OprOpsPerPart:number,
   OprProdCrewSize:number,
   OprStartDate:string,
   OprDueDate:string,
   OprMachines:number,
   ActEmp:string,
   JobComments:string,
   AsmComments:string,
   OprComments:string,
   JobNum:string,
   Asm:number,
   Opr:number,
   JobAsmOpr:string,
   OprInstructions:string,
   OprQtyPerCycle:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobAddlInfoTableset{
   JobAddlInfo:Erp_Tablesets_JobAddlInfoRow[],
   JobOperAction:Erp_Tablesets_JobOperActionRow[],
   JobOperActionParam:Erp_Tablesets_JobOperActionParamRow[],
   JobAddInfoDtl:Erp_Tablesets_JobAddInfoDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_JobOperActionParamRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Job Number.  */  
   JobNum:string,
      /**  A sequence number which uniquely identifies the assembly record within the method.  */  
   AssemblySeq:number,
      /**  A sequence number which uniquely identifies the operation record within the method.  */  
   OprSeq:number,
      /**  A sequence number which uniquely identifies action record within the operation set.  */  
   ActionSeq:number,
      /**  A sequence number which uniquely identifies parameter within the Operation/Action set.  */  
   ActionParamSeq:number,
      /**  Data type of Action Parameter.  */  
   ActionParamFieldDataType:string,
      /**  Value of Action Parameter.  */  
   ActionParamValueCharacter:string,
      /**  Value of Action Parameter.  */  
   ActionParamValueDate:string,
      /**  Value of Action Parameter.  */  
   ActionParamValueDecimal:number,
      /**  Value of Action Parameter.  */  
   ActionParamValueInteger:number,
      /**  Value of Action Parameter.  */  
   ActionParamValueLogical:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobOperActionRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Job Number.  */  
   JobNum:string,
      /**  A sequence number which uniquely identifies the assembly record within the method.  */  
   AssemblySeq:number,
      /**  A sequence number which uniquely identifies the operation record within the method.  */  
   OprSeq:number,
      /**  A sequence number which uniquely identifies action record within the operation set.  */  
   ActionSeq:number,
      /**  Description of Action.  */  
   ActionDesc:string,
      /**  Indicated if this action must be completed before Operation can be completed.  */  
   Required:boolean,
      /**  Indicates if this Action was completed.  */  
   Completed:boolean,
      /**  The number of the employee that performed the work.  */  
   CompletedBy:string,
      /**  Date the Action was completed.  */  
   CompletedOn:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
   EmpBasicName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OpMasterListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   OpCode:string,
      /**  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  */  
   OpDesc:string,
      /**  Identifies the Buyer for the subcontract operation.  Used as the default in the Automated Purchasing process.  */  
   BuyerID:string,
   BuyerName:string,
      /**  Operation Type - "SRV" Service Call Operation
                           "MFG" Manufacturing operation  */  
   OPType:string,
   AllowInCurPlant:boolean,
      /**  SubContract Operation  */  
   Subcontract:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Operation has Characteristics  */  
   HasCharacteristics:boolean,
      /**  Operations has some Actions.  */  
   HasActions:boolean,
      /**  ID of related Attribute Class, the class must be of type Characteristics.  */  
   CharacteristicAttrClassID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   CharacteristicAttributeSetID:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OperationsTableset{
   OpMasterList:Erp_Tablesets_OpMasterListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ResourceGroupListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  A code uniquely identifies a Resource Group.  Cannot be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   ResourceGrpID:string,
      /**  Long description of the Resource Group.  */  
   Description:string,
      /**   Flag which indicates if the Resource Group is considered "Inactive".  For historical purposed, and data integrity, it is difficult to delete a ResourceGroup that has been used for production.  Instead, it is set to Inactive = YES.
This flag will be used to exclude Resource Groups from certain searches and reports.
Resource Groups where Inactive=yes are treated as deleted, but remain in the table to maintain database integrity.  */  
   Inactive:boolean,
      /**  The Key ID of the Home Department for this Resource Group.  This is a foreign key to the JCDept table.  */  
   JCDept:string,
      /**  The burden rate for production.  */  
   ProdBurRate:number,
      /**  Default burden rate for Setup time.  */  
   SetupBurRate:number,
      /**   Quoting burden rate for production in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   QProdBurRate:number,
      /**   Quoting burden rate for setup in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  */  
   QSetupBurRate:number,
      /**  For scheduling purposes a Resource Group can be a Standard resource (S), Additional resource (D), or Auxiliary resource (X).  Standard resources use capacity when scheduled in a finite capacity workcenter.  An Auxiliary Resource can be used in production by  any operation concurrently with a Standard resource, but it does not use capacity.  This is significant for scheduling work to the machine.  Also, an Auxiliary resources does not have to be available for an entire operation.  Additional resources can be added to an Operation, they do use capacity and need to be available for the entire operation.  */  
   ResourceType:string,
      /**  Indicates a warehouse  in which parts are staged for consumption by the Resource Group.  This must be valid in the Warehouse table.  */  
   InputWhse:string,
      /**  Defines a warehouse for the output of a Resource Group.  This must be valid in the Warehouse table.  */  
   OutputWhse:string,
      /**  Location  */  
   Location:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ID of related Attribute Class, the class must be of type Characteristics.  */  
   CharacteristicAttrClassID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   CharacteristicAttributeSetID:number,
   JCDeptDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ResourceGroupsTableset{
   ResourceGroupList:Erp_Tablesets_ResourceGroupListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipJobNum
      @param ipAssemblySeq
      @param ipOprSeq
      @param ipCrewCount
   */  
export interface GetJobInfo_input{
      /**  Job number  */  
   ipJobNum:string,
      /**  Assembly Seq  */  
   ipAssemblySeq:number,
      /**  Opr Seq  */  
   ipOprSeq:number,
      /**  Crew Count  */  
   ipCrewCount:number,
}

export interface GetJobInfo_output{
   returnObj:Erp_Tablesets_JobAddlInfoTableset[],
}

export interface GetOperations_output{
   returnObj:Erp_Tablesets_OperationsTableset[],
}

export interface GetResourceGroups_output{
   returnObj:Erp_Tablesets_ResourceGroupsTableset[],
}

export interface Ice_Extensions_ExtensionRow{
   ColumnValues:object
   RowMod:string,
   SysRowID:string,
}

export interface Ice_Extensions_ExtensionTableColumn{
   ColumnName:string,
   ColumnType:string,
}

export interface Ice_Extensions_ExtensionTableData{
   Table:Ice_Extensions_ExtensionRow[],
   SystemCode:string,
   TableName:string,
   Columns:Ice_Extensions_ExtensionTableColumn[],
   PrimaryKeyColumns:string,
   PeerTableSystemCode:string,
   PeerTableName:string,
}

export interface Overrides_output{
}

