import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.JobAsmblCostsSvc
// Description: Logic to retrieve Hours and Costs for Job Assemblies
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmblCostsSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmblCostsSvc/$metadata", {
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
   Summary: Invoke method GetJobAsmblCosts
   Description: Retrieves the Hours and Costs for a Job Assembly
   OperationID: GetJobAsmblCosts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJobAsmblCosts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJobAsmblCosts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetJobAsmblCosts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmblCostsSvc/GetJobAsmblCosts", {
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



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Erp_Tablesets_JobAsmblCostsTableset{
   JobCosts:Erp_Tablesets_JobCostsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_JobCostsRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Job Number  */  
   JobNum:string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  */  
   AssemblySeq:number,
      /**  Lower Level Burden Labor Cost.  */  
   LLABurdenCost:number,
      /**  Lower Level Actual Labor Cost.  */  
   LLALaborCost:number,
      /**  Lower Level Actual Material Burden Cost.  */  
   LLAMaterialBurCost:number,
      /**  Lower Level Actual Material Cost.  */  
   LLAMaterialCost:number,
      /**  Lower Level Actual Material Labor Cost. LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost = LLAMaterialCost.  */  
   LLAMaterialLabCost:number,
      /**  Lower Level Actual Material Material Cost. LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost = LLAMaterialCost.  */  
   LLAMaterialMtlCost:number,
      /**  Lower Level Actual Material Subcontract Cost. LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost = LLAMaterialCost.  */  
   LLAMaterialSubCost:number,
      /**  Lower Level Actual Material Burden Cost.  */  
   LLAMtlBurCost:number,
      /**  Lower Level Actual Production Hours.  */  
   LLAProdHours:number,
      /**  Lower Level Actual Setup Hours.  */  
   LLASetupHours:number,
      /**  Lower Level Actual Subcontractor Cost.  */  
   LLASubcontractCost:number,
      /**  Lower Level Estimated Burden Cost.  */  
   LLEBurdenCost:number,
      /**  Lower Level Estimated Labor Cost.  */  
   LLELaborCost:number,
      /**  Lower Level Estimated Material Cost.  */  
   LLEMaterialCost:number,
      /**  Lower Level Estimated Material Burden Cost.  */  
   LLEMtlBurCost:number,
      /**  Lower Level Est Prod. Hrs  */  
   LLEProdHours:number,
      /**  Lower Level Estimated Setup Hours.  */  
   LLESetupHours:number,
      /**  Lower Level Estimated Subcontract Cost.  */  
   LLESubcontractCost:number,
      /**  Asembly Total Actual Production Hours (TLAProdHours + LLAProdHours)  */  
   PActTotalHours:number,
      /**  Assembly Total Estimated Production Hours (TLEProdHours + LLEProdHours)  */  
   PEstTotalHours:number,
      /**  Assembly Total Actual Setup Hours (TLASetupHours + LLASetupHours)  */  
   SActTotalHours:number,
      /**  Assembly Total Estimated Setup Hours (TLESetupHours + LLESetupHours)  */  
   SEstTotalHours:number,
      /**  Burden Actual Assembly Totals (TLABurdenCost + LLABurdenCost)  */  
   TActBurCost:number,
      /**  Labor Actual Assembly Totals (TLALaborCost + LLALaborCost)  */  
   TActLabCost:number,
      /**  Lower Level Actual Total Hours (LLASetupHours + LLAProdHours)  */  
   TActLowerHours:number,
      /**  Material Burden Actual Assembly Totals (TLAMtlBurCost + LLAMtlBurCost)  */  
   TActMtlBurCost:number,
      /**  Material Actual Assembly Totals (TLAMaterialCost + LLAMaterialCost)  */  
   TActMtlCost:number,
      /**  Subcontract Actual Assembly Totals (TLASubcontractCost + LLASubcontractCost)  */  
   TActSubCost:number,
      /**  This Level Actual Total Hours (TLASetupHours + TLAProdHours)  */  
   TActThisHours:number,
      /**  Total Actual Assembly Totals (TActMtlCost + TActLabCost + TActBurCost + TActSubCost + TActMtlBurCost)  */  
   TActTotalCost:number,
      /**  Assembly Total Actual Total Hours (SActTotalHours + PActTotalHours)  */  
   TActTotalHours:number,
      /**  Burden Detail Assembly Totals  */  
   TDtlBurCost:number,
      /**  Labor Detail Assembly Totals  */  
   TDtlLabCost:number,
      /**  Material Burden Detail Assembly Totals  */  
   TDtlMtlBurCost:number,
      /**  Material Detail Assembly Totals  */  
   TDtlMtlCost:number,
      /**  Subcontract Detail Assembly Totals  */  
   TDtlSubCost:number,
      /**  Burden Estimated Assembly Totals (TLEBurdenCost + LLEBurdenCost)  */  
   TEstBurCost:number,
      /**  Labor Estimated Assembly Totals (TLELaborCost + LLELaborCost)  */  
   TEstLabCost:number,
      /**  Lower Level Estimated Total Hours (LLESetupHours + LLEProdHours)  */  
   TEstLowerHours:number,
      /**  Material Burden Estimated Assembly Totals (TLEMtlBurCost + LLEMtlBurCost)  */  
   TEstMtlBurCost:number,
      /**  Material Estimated Assembly Totals (TLEMaterialCost + LLEMaterialCost)  */  
   TEstMtlCost:number,
      /**  Subcontract Estimated Assembly Totals (TLESubcontractCost + LLESubcontractCost)  */  
   TEstSubCost:number,
      /**  This Level Estimated Total Hours (TLESetupHours + TLEProdHours)  */  
   TEstThisHours:number,
      /**  Total Estimated Assembly Totals (TEstMtlCost + TEstLabCost + TEstBurCost + TEstSubCost + TEstMtlBurCost)  */  
   TEstTotalCost:number,
      /**  Assembly Total Estimated Total Hours (SEstTotalHours + PEstTotalHours)  */  
   TEstTotalHours:number,
      /**  This Level Actual Burden Cost.  */  
   TLABurdenCost:number,
      /**  This Level Actual Labor Cost  */  
   TLALaborCost:number,
      /**  This Level Actual Material Burden Cost. TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost = TLAMaterialCost.  */  
   TLAMaterialBurCost:number,
      /**  This Level Actual Material Cost  */  
   TLAMaterialCost:number,
      /**  Lower Level Actual Material Labor Cost. LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost = LLAMaterialCost.  */  
   TLAMaterialLabCost:number,
      /**  This Level Actual Material Mtl. Cost  */  
   TLAMaterialMtlCost:number,
      /**  Lower Level Actual Material Subcontract Cost. LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost = LLAMaterialCost.  */  
   TLAMaterialSubCost:number,
      /**  This Level Actual Material Burden Cost  */  
   TLAMtlBurCost:number,
      /**  This Level Actual Prod. Hrs  */  
   TLAProdHours:number,
      /**  This Level Actual Setup Hours.  */  
   TLASetupHours:number,
      /**  This Level Actual Subcontract Cost.  */  
   TLASubcontractCost:number,
      /**  This Level Est Burden Cost  */  
   TLEBurdenCost:number,
      /**  This Level Est Labor Cost  */  
   TLELaborCost:number,
      /**  This Level Estimated Material Cost.  */  
   TLEMaterialCost:number,
      /**  This Level Est Material Burden Cost  */  
   TLEMtlBurCost:number,
      /**  This Level Estimated Production Hours.  */  
   TLEProdHours:number,
      /**  This Level Estimated Setup Hours.  */  
   TLESetupHours:number,
      /**  This Level Est Subcontract Cost  */  
   TLESubcontractCost:number,
      /**  This Level Actual Component Material Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for this level.  Otherwise, TLAMaterialMtlBurCost may be populated but is not included in the calculation of TLAMaterialCost.  */  
   TLAMaterialMtlBurCost:number,
      /**  Lower Level Actual Component Material Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for the lower level.  Otherwise, LLAMaterialMtlBurCost may be populated but is not included in the calculation of LLAMaterialCost.  */  
   LLAMaterialMtlBurCost:number,
      /**  Lower Level Material Cost Element.  This is the difference between the Actual Material Cost (LLAMaterialCost) and the Component Material Cost (LLAMaterialMtlCost).  */  
   LLCMaterialCost:number,
      /**  Lower Level Labor Cost Element.  This is the difference between the Actual Labor Cost (LLALaborCost) and the Component Labor Cost (LLAMaterialLabCost).  */  
   LLCLaborCost:number,
      /**  Lower Level Burden Cost Element.  This is the difference between the Actual Burden Cost (LLABurdenCost) and the Component Burden Cost (LLAMaterialBurCost).  */  
   LLCBurdenCost:number,
      /**  Lower Level Subcontract Cost Element.  This is the difference between the Actual Subcontract Cost (LLASubcontractCost) and the Component Subcontract Cost (LLAMaterialSubCost).  */  
   LLCSubcontractCost:number,
      /**  Lower Level Material Cost Element.  This is the difference between the Actual Material Burden Cost (LLAMtlBurCost) and the Component Material Burden Cost (LLAMaterialMtlBurCost).  */  
   LLCMtlBurCost:number,
      /**  Material Cost Element Assembly Totals (TActMtlCost - TDtlMtlCost)  */  
   TCmpMaterialCost:number,
      /**  Labor Cost Element Assembly Totals (TActLabCost - TDtlLabCost)  */  
   TCmpLaborCost:number,
      /**  Burden Cost Element Assembly Totals (TActBurCost - TDtlBurCost)  */  
   TCmpBurdenCost:number,
      /**  Subcontract Cost Element Assembly Totals (TActSubCost - TDtlSubCost)  */  
   TCmpSubcontractCost:number,
      /**  Material Burden Cost Element Assembly Totals (TActMtlBurCost - TDtlMtlBurCost)  */  
   TCmpMtlBurCost:number,
      /**  This Level Material Cost Element.  This is the difference between the Actual Material Cost (TLAMaterialCost) and the Component Material Cost (TLAMaterialMtlCost).  */  
   TLCMaterialCost:number,
      /**  This Level Labor Cost Element.  This is the difference between the Actual Labor Cost (TLALaborCost) and the Component Labor Cost (TLAMaterialLabCost).  */  
   TLCLaborCost:number,
      /**  This Level Burden Cost Element.  This is the difference between the Actual Burden Cost (TLABurdenCost) and the Component Burden Cost (TLAMaterialBurCost).  */  
   TLCBurdenCost:number,
      /**  This Level Subcontract Cost Element.  This is the difference between the Actual Subcontract Cost (TLASubcontractCost) and the Component Subcontract Cost (TLAMaterialSubCost).  */  
   TLCSubcontractCost:number,
      /**  This Level Material Burden Cost Element.  This is the difference between the Actual Material Burden Cost (TLAMtlBurCost) and the Component Material Burden Cost (TLAMaterialMtlBurCost).  */  
   TLCMtlBurCost:number,
      /**  Lower Level Actual Mfg Component Material Cost.  */  
   LLAMfgCompMtlCost:number,
      /**  Lower Level Actual Mfg Component Labor Cost.  */  
   LLAMfgCompLabCost:number,
      /**  Lower Level Actual Mfg Component Burden Cost.  */  
   LLAMfgCompBurCost:number,
      /**  Lower Level Actual Mfg Component Subcontract Cost.  */  
   LLAMfgCompSubCost:number,
      /**  Lower Level Actual Mfg Component Material Burden Cost.  */  
   LLAMfgCompMtlBurCost:number,
      /**  This Level Actual Mfg Component Material Cost.  */  
   TLAMfgCompMtlCost:number,
      /**  This Level Actual Mfg Component Labor Cost.  */  
   TLAMfgCompLabCost:number,
      /**  This Level Actual Mfg Component Burden Cost.  */  
   TLAMfgCompBurCost:number,
      /**  This Level Actual Mfg Component Subcontract Cost.  */  
   TLAMfgCompSubCost:number,
      /**  This Level Actual Mfg Component Material Burden Cost.  */  
   TLAMfgCompMtlBurCost:number,
      /**  Burden Mfg Element Assembly Totals (TLAMfgCompBurCost + LLAMfgCompBurCost)  */  
   TMfgBurCost:number,
      /**  Labor Mfg Element Assembly Totals (TLAMfgCompLabCost + LLAMfgCompLabCost)  */  
   TMfgLabCost:number,
      /**  Material Mfg Element Assembly Totals (TLAMfgCompMtlCost + LLAMfgCompMtlCost)  */  
   TMfgMtlCost:number,
      /**  Material Burden Mfg Element Assembly Totals (TLAMfgCompMtlBurCost + LLAMfgCompMtlBurCost)  */  
   TMfgMtlBurCost:number,
      /**  Subcontract Mfg Element Assembly Totals (TLAMfgCompSubCost + LLAMfgCompSubCost)  */  
   TMfgSubCost:number,
      /**  TLE Total Cost  */  
   TLETotalCost:number,
      /**  TLС Total Cost  */  
   TLСTotalCost:number,
      /**  TLA Total Cost  */  
   TLATotalCost:number,
      /**  TLAMfgComp Total Cost  */  
   TLAMfgCompTotalCost:number,
      /**  TLA Material Total Cost  */  
   TLAMaterialTotalCost:number,
      /**  LLE Total Cost  */  
   LLETotalCost:number,
      /**  LLC Total Cost  */  
   LLCTotalCost:number,
      /**  LLA Total Cost  */  
   LLATotalCost:number,
      /**  LLA  MfgComp Total Cost  */  
   LLAMfgCompTotalCost:number,
      /**  LLA Material Total Cost  */  
   LLAMaterialTotalCost:number,
      /**  TCmp Total Cost  */  
   TCmpTotalCost:number,
      /**  TMfg Total Cost  */  
   TMfgTotalCost:number,
      /**  TDtl Total Cost  */  
   TDtlTotalCost:number,
      /**  TLC Total Cost  */  
   TLCTotalCost:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ipJobNum
      @param ipAssemblySeq
   */  
export interface GetJobAsmblCosts_input{
      /**  Job Number  */  
   ipJobNum:string,
      /**  Assembly Sequence  */  
   ipAssemblySeq:number,
}

export interface GetJobAsmblCosts_output{
   returnObj:Erp_Tablesets_JobAsmblCostsTableset[],
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

