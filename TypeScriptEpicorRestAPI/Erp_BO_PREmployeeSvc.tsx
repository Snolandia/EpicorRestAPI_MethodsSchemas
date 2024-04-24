import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PREmployeeSvc
// Description: Payroll Employee Maintenance consists of:
1) Payroll Employee Deduction master.
This file establishes which deduction, the amount of deduction
and when it is to be taken for a specific employee.
2)Payroll Employee master.
This file is an extension of the data stored in the EmpBasic file.
All of the data fields stored in EmpBasic also exist in PREmpMas.
They are kept in sync via write triggers on both the EmpBasic/PREmpMas.
The existence of this record indicates that this employee is set up in the payroll system.
3) Payroll employee master rate file.
4) Payroll Employee Tax file.
Establishes the different taxes that are relevant for an employee.
Subset to the PREmpMas file.
Notes: 2 of sort options are based on the PREmpMas.Terminated Flag
The 3rd sort option browses on the EmpBasic table where PRSetupReq is true
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/$metadata", {
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get PREmployees items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PREmployees
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PREmpMasRow
   */  
export function get_PREmployees(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpMasRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpMasRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PREmployees
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PREmpMasRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PREmpMasRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PREmployees(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees", {
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
   Summary: Calls GetByID to retrieve the PREmployee item
   Description: Calls GetByID to retrieve the PREmployee item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PREmployee
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PREmpMasRow
   */  
export function get_PREmployees_Company_EmpID(Company:string, EmpID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PREmpMasRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PREmpMasRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PREmployee for the service
   Description: Calls UpdateExt to update PREmployee. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PREmployee
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PREmpMasRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PREmployees_Company_EmpID(Company:string, EmpID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete PREmployee item
   Description: Call UpdateExt to delete PREmployee item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PREmployee
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PREmployees_Company_EmpID(Company:string, EmpID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")", {
          method: 'delete',
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
   Summary: Calls GetByID for the service
   Description: Get PREmpDeds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PREmpDeds1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PREmpDedRow
   */  
export function get_PREmployees_Company_EmpID_PREmpDeds(Company:string, EmpID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpDedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")/PREmpDeds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpDedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PREmpDed item
   Description: Calls GetByID to retrieve the PREmpDed item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PREmpDed1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpLink Desc: EmpLink   Required: True   Allow empty value : True
      @param DeductionID Desc: DeductionID   Required: True   Allow empty value : True
      @param DeductionNum Desc: DeductionNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PREmpDedRow
   */  
export function get_PREmployees_Company_EmpID_PREmpDeds_Company_EmpLink_DeductionID_DeductionNum(Company:string, EmpID:string, EmpLink:string, DeductionID:string, DeductionNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PREmpDedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")/PREmpDeds(" + Company + "," + EmpLink + "," + DeductionID + "," + DeductionNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PREmpDedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PREmpRts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PREmpRts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PREmpRtRow
   */  
export function get_PREmployees_Company_EmpID_PREmpRts(Company:string, EmpID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpRtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")/PREmpRts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpRtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PREmpRt item
   Description: Calls GetByID to retrieve the PREmpRt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PREmpRt1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpLink Desc: EmpLink   Required: True   Allow empty value : True
      @param RateDate Desc: RateDate   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PREmpRtRow
   */  
export function get_PREmployees_Company_EmpID_PREmpRts_Company_EmpLink_RateDate(Company:string, EmpID:string, EmpLink:string, RateDate:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PREmpRtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")/PREmpRts(" + Company + "," + EmpLink + "," + RateDate + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PREmpRtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PREmpTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PREmpTaxes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PREmpTaxRow
   */  
export function get_PREmployees_Company_EmpID_PREmpTaxes(Company:string, EmpID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")/PREmpTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PREmpTax item
   Description: Calls GetByID to retrieve the PREmpTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PREmpTax1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param EmpLink Desc: EmpLink   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PREmpTaxRow
   */  
export function get_PREmployees_Company_EmpID_PREmpTaxes_Company_EmpLink_TaxTblID(Company:string, EmpID:string, EmpLink:string, TaxTblID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PREmpTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")/PREmpTaxes(" + Company + "," + EmpLink + "," + TaxTblID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PREmpTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   */  
export function get_PREmployees_Company_EmpID_EntityGLCs(Company:string, EmpID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")/EntityGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   */  
export function get_PREmployees_Company_EmpID_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, EmpID:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PREmpMasAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PREmpMasAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PREmpMasAttchRow
   */  
export function get_PREmployees_Company_EmpID_PREmpMasAttches(Company:string, EmpID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpMasAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")/PREmpMasAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpMasAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PREmpMasAttch item
   Description: Calls GetByID to retrieve the PREmpMasAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PREmpMasAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PREmpMasAttchRow
   */  
export function get_PREmployees_Company_EmpID_PREmpMasAttches_Company_EmpID_DrawingSeq(Company:string, EmpID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PREmpMasAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmployees(" + Company + "," + EmpID + ")/PREmpMasAttches(" + Company + "," + EmpID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PREmpMasAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PREmpDeds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PREmpDeds
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PREmpDedRow
   */  
export function get_PREmpDeds(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpDedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpDeds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpDedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PREmpDeds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PREmpDedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PREmpDedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PREmpDeds(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpDeds", {
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
   Summary: Calls GetByID to retrieve the PREmpDed item
   Description: Calls GetByID to retrieve the PREmpDed item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PREmpDed
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpLink Desc: EmpLink   Required: True   Allow empty value : True
      @param DeductionID Desc: DeductionID   Required: True   Allow empty value : True
      @param DeductionNum Desc: DeductionNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PREmpDedRow
   */  
export function get_PREmpDeds_Company_EmpLink_DeductionID_DeductionNum(Company:string, EmpLink:string, DeductionID:string, DeductionNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PREmpDedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpDeds(" + Company + "," + EmpLink + "," + DeductionID + "," + DeductionNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PREmpDedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PREmpDed for the service
   Description: Calls UpdateExt to update PREmpDed. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PREmpDed
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpLink Desc: EmpLink   Required: True   Allow empty value : True
      @param DeductionID Desc: DeductionID   Required: True   Allow empty value : True
      @param DeductionNum Desc: DeductionNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PREmpDedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PREmpDeds_Company_EmpLink_DeductionID_DeductionNum(Company:string, EmpLink:string, DeductionID:string, DeductionNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpDeds(" + Company + "," + EmpLink + "," + DeductionID + "," + DeductionNum + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete PREmpDed item
   Description: Call UpdateExt to delete PREmpDed item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PREmpDed
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpLink Desc: EmpLink   Required: True   Allow empty value : True
      @param DeductionID Desc: DeductionID   Required: True   Allow empty value : True
      @param DeductionNum Desc: DeductionNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PREmpDeds_Company_EmpLink_DeductionID_DeductionNum(Company:string, EmpLink:string, DeductionID:string, DeductionNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpDeds(" + Company + "," + EmpLink + "," + DeductionID + "," + DeductionNum + ")", {
          method: 'delete',
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
   Summary: Calls GetRows for the service
   Description: Get PREmpRts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PREmpRts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PREmpRtRow
   */  
export function get_PREmpRts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpRtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpRts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpRtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PREmpRts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PREmpRtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PREmpRtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PREmpRts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpRts", {
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
   Summary: Calls GetByID to retrieve the PREmpRt item
   Description: Calls GetByID to retrieve the PREmpRt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PREmpRt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpLink Desc: EmpLink   Required: True   Allow empty value : True
      @param RateDate Desc: RateDate   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PREmpRtRow
   */  
export function get_PREmpRts_Company_EmpLink_RateDate(Company:string, EmpLink:string, RateDate:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PREmpRtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpRts(" + Company + "," + EmpLink + "," + RateDate + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PREmpRtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PREmpRt for the service
   Description: Calls UpdateExt to update PREmpRt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PREmpRt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpLink Desc: EmpLink   Required: True   Allow empty value : True
      @param RateDate Desc: RateDate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PREmpRtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PREmpRts_Company_EmpLink_RateDate(Company:string, EmpLink:string, RateDate:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpRts(" + Company + "," + EmpLink + "," + RateDate + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete PREmpRt item
   Description: Call UpdateExt to delete PREmpRt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PREmpRt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpLink Desc: EmpLink   Required: True   Allow empty value : True
      @param RateDate Desc: RateDate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PREmpRts_Company_EmpLink_RateDate(Company:string, EmpLink:string, RateDate:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpRts(" + Company + "," + EmpLink + "," + RateDate + ")", {
          method: 'delete',
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
   Summary: Calls GetRows for the service
   Description: Get PREmpTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PREmpTaxes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PREmpTaxRow
   */  
export function get_PREmpTaxes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PREmpTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PREmpTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PREmpTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PREmpTaxes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpTaxes", {
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
   Summary: Calls GetByID to retrieve the PREmpTax item
   Description: Calls GetByID to retrieve the PREmpTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PREmpTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpLink Desc: EmpLink   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PREmpTaxRow
   */  
export function get_PREmpTaxes_Company_EmpLink_TaxTblID(Company:string, EmpLink:string, TaxTblID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PREmpTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpTaxes(" + Company + "," + EmpLink + "," + TaxTblID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PREmpTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PREmpTax for the service
   Description: Calls UpdateExt to update PREmpTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PREmpTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpLink Desc: EmpLink   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PREmpTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PREmpTaxes_Company_EmpLink_TaxTblID(Company:string, EmpLink:string, TaxTblID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpTaxes(" + Company + "," + EmpLink + "," + TaxTblID + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete PREmpTax item
   Description: Call UpdateExt to delete PREmpTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PREmpTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpLink Desc: EmpLink   Required: True   Allow empty value : True
      @param TaxTblID Desc: TaxTblID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PREmpTaxes_Company_EmpLink_TaxTblID(Company:string, EmpLink:string, TaxTblID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpTaxes(" + Company + "," + EmpLink + "," + TaxTblID + ")", {
          method: 'delete',
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
   Summary: Calls GetRows for the service
   Description: Get EntityGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EntityGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   */  
export function get_EntityGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/EntityGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EntityGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EntityGLCs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/EntityGLCs", {
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
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   */  
export function get_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EntityGLC for the service
   Description: Calls UpdateExt to update EntityGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete EntityGLC item
   Description: Call UpdateExt to delete EntityGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'delete',
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
   Summary: Calls GetRows for the service
   Description: Get PREmpMasAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PREmpMasAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PREmpMasAttchRow
   */  
export function get_PREmpMasAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpMasAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpMasAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpMasAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PREmpMasAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PREmpMasAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PREmpMasAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PREmpMasAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpMasAttches", {
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
   Summary: Calls GetByID to retrieve the PREmpMasAttch item
   Description: Calls GetByID to retrieve the PREmpMasAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PREmpMasAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PREmpMasAttchRow
   */  
export function get_PREmpMasAttches_Company_EmpID_DrawingSeq(Company:string, EmpID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PREmpMasAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpMasAttches(" + Company + "," + EmpID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PREmpMasAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PREmpMasAttch for the service
   Description: Calls UpdateExt to update PREmpMasAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PREmpMasAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PREmpMasAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PREmpMasAttches_Company_EmpID_DrawingSeq(Company:string, EmpID:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpMasAttches(" + Company + "," + EmpID + "," + DrawingSeq + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete PREmpMasAttch item
   Description: Call UpdateExt to delete PREmpMasAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PREmpMasAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PREmpMasAttches_Company_EmpID_DrawingSeq(Company:string, EmpID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/PREmpMasAttches(" + Company + "," + EmpID + "," + DrawingSeq + ")", {
          method: 'delete',
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
   Summary: Calls GetRows for the service
   Description: Get Partners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Partners
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartnerRow
   */  
export function get_Partners(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartnerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/Partners", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartnerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Partners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartnerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartnerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Partners(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/Partners", {
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
   Summary: Calls GetByID to retrieve the Partner item
   Description: Calls GetByID to retrieve the Partner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Partner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartnerNum Desc: PartnerNum   Required: True
      @param PartnerType Desc: PartnerType   Required: True
      @param PartnerID Desc: PartnerID   Required: True   Allow empty value : True
      @param SearchID Desc: SearchID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartnerRow
   */  
export function get_Partners_Company_PartnerNum_PartnerType_PartnerID_SearchID(Company:string, PartnerNum:string, PartnerType:string, PartnerID:string, SearchID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartnerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PartnerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Partner for the service
   Description: Calls UpdateExt to update Partner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Partner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartnerNum Desc: PartnerNum   Required: True
      @param PartnerType Desc: PartnerType   Required: True
      @param PartnerID Desc: PartnerID   Required: True   Allow empty value : True
      @param SearchID Desc: SearchID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartnerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Partners_Company_PartnerNum_PartnerType_PartnerID_SearchID(Company:string, PartnerNum:string, PartnerType:string, PartnerID:string, SearchID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete Partner item
   Description: Call UpdateExt to delete Partner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Partner
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartnerNum Desc: PartnerNum   Required: True
      @param PartnerType Desc: PartnerType   Required: True
      @param PartnerID Desc: PartnerID   Required: True   Allow empty value : True
      @param SearchID Desc: SearchID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Partners_Company_PartnerNum_PartnerType_PartnerID_SearchID(Company:string, PartnerNum:string, PartnerType:string, PartnerID:string, SearchID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")", {
          method: 'delete',
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
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PREmpMasListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpMasListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpMasListRow)
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
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClausePREmpMas:string, whereClausePREmpMasAttch:string, whereClausePREmpDed:string, whereClausePREmpRt:string, whereClausePREmpTax:string, whereClauseEntityGLC:string, whereClausePartner:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePREmpMas!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePREmpMas=" + whereClausePREmpMas
   }
   if(typeof whereClausePREmpMasAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePREmpMasAttch=" + whereClausePREmpMasAttch
   }
   if(typeof whereClausePREmpDed!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePREmpDed=" + whereClausePREmpDed
   }
   if(typeof whereClausePREmpRt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePREmpRt=" + whereClausePREmpRt
   }
   if(typeof whereClausePREmpTax!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePREmpTax=" + whereClausePREmpTax
   }
   if(typeof whereClauseEntityGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEntityGLC=" + whereClauseEntityGLC
   }
   if(typeof whereClausePartner!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartner=" + whereClausePartner
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/GetRows" + params, {
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

   /**  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(empID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof empID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "empID=" + empID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/GetByID" + params, {
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

   /**  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      @param whereClause Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/GetList" + params, {
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

   /**  
   Summary: Invoke method AddEmployeeResultsLinkCompany
   Description: This method will add employee results link to all employees in the company
   OperationID: AddEmployeeResultsLinkCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddEmployeeResultsLinkCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddEmployeeResultsLinkCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddEmployeeResultsLinkCompany(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/AddEmployeeResultsLinkCompany", {
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
   Summary: Invoke method BuildClassList
   Description: This method returns a list of valid Classes to select from for the user's security
   OperationID: BuildClassList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildClassList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildClassList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/BuildClassList", {
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
   Summary: Invoke method BuildFilingList
   Description: This method returns a list of filing status' based on the TaxTable ID selected
   OperationID: BuildFilingList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildFilingList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildFilingList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildFilingList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/BuildFilingList", {
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
   Summary: Invoke method BuildTaxTblList
   Description: This method generates a list of TaxTbls available to choose from when Adding/Updating
a PREmpTax record
   OperationID: BuildTaxTblList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildTaxTblList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildTaxTblList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildTaxTblList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/BuildTaxTblList", {
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
   Summary: Invoke method CalcSalaryRate
   Description: This method updates the salary or rate field on PREmpRt when the other field is updated
It is to be run after either Salary or PayRate is updated.
   OperationID: CalcSalaryRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcSalaryRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcSalaryRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalcSalaryRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/CalcSalaryRate", {
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
   Summary: Invoke method ChangeFileStatus
   Description: This method should run when the JobMtl.Plant field changes.
This method determines the default JobMtl.WarehouseCode associated with the new JobMtl.Plant.
   OperationID: ChangeFileStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFileStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFileStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFileStatus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/ChangeFileStatus", {
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
   Summary: Invoke method CheckPayRateEffectiveDate
   Description: This method checks if the first pay rate effective date is different than the hire date.  Returns an
informational message if it is.
   OperationID: CheckPayRateEffectiveDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPayRateEffectiveDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPayRateEffectiveDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPayRateEffectiveDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/CheckPayRateEffectiveDate", {
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
   Summary: Invoke method CheckPersonContact
   Description: Checks if the Person Contact ID is already assigned to another Payroll Employee
   OperationID: CheckPersonContact
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPersonContact_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPersonContact_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPersonContact(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/CheckPersonContact", {
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
   Summary: Invoke method CheckJCDeptExists
   Description: This method checks if the JCDept record exists.
   OperationID: CheckJCDeptExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckJCDeptExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckJCDeptExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckJCDeptExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/CheckJCDeptExists", {
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
   Summary: Invoke method CheckLaborExpCodeExists
   Description: This method checks if the LabExpCd record exists.
   OperationID: CheckLaborExpCodeExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckLaborExpCodeExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckLaborExpCodeExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckLaborExpCodeExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/CheckLaborExpCodeExists", {
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
   Summary: Invoke method CheckLeavePREmpMas
   Description: This method checks if a PREmpRt record exists for the current employee record
if no record exists then the user cannot leave the record until they create a rate
record or delete the employee record.
   OperationID: CheckLeavePREmpMas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckLeavePREmpMas_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckLeavePREmpMas_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckLeavePREmpMas(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/CheckLeavePREmpMas", {
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
   Summary: Invoke method CheckPRClassExisst
   Description: This method checks if the PRClass record exists.
   OperationID: CheckPRClassExisst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPRClassExisst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPRClassExisst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPRClassExisst(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/CheckPRClassExisst", {
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
   Summary: Invoke method CheckPRWorkCompCodeExists
   Description: This method checks if the PRWrkCmp record exists.
   OperationID: CheckPRWorkCompCodeExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPRWorkCompCodeExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPRWorkCompCodeExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPRWorkCompCodeExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/CheckPRWorkCompCodeExists", {
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
   Summary: Invoke method GetDeductDefaults
   Description: This method sets the deduction defaults once the DeductionID is selected
   OperationID: GetDeductDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDeductDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDeductDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDeductDefaults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/GetDeductDefaults", {
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
   Summary: Invoke method GetEmpIDInfo
   Description: This method will default the name and address information from EmpBasic if
the EmpId entered exists in EmpBasic
   OperationID: GetEmpIDInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEmpIDInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEmpIDInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEmpIDInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/GetEmpIDInfo", {
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
   Summary: Invoke method GetEmpLinkValue
   Description: Gets Employee Link
   OperationID: GetEmpLinkValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEmpLinkValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEmpLinkValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEmpLinkValue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/GetEmpLinkValue", {
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
   Summary: Invoke method GetNewShopEmployee
   Description: This method creates a new PREmpMas record based on information from the EmpBasic record. It
takes EmpID as a parameter.
The standard GetNewPREmpMas method will be used when adding a new Payroll Employee from scratch.
   OperationID: GetNewShopEmployee
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShopEmployee_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShopEmployee_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewShopEmployee(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/GetNewShopEmployee", {
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
   Summary: Invoke method GetOverrideList
   Description: This method is identical to the GetList method except that it overrides the
PREmpMas find trigger and will return all Employees, not just the ones the user has
clearance for.  This is mainly for the SupervisorID lookups for Shop and Payroll employee
maintenance
   OperationID: GetOverrideList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOverrideList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOverrideList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOverrideList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/GetOverrideList", {
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
   Summary: Invoke method GetPerConData
   OperationID: GetPerConData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPerConData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPerConData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPerConData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/GetPerConData", {
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
   Summary: Invoke method GetShopEmployeeInfo
   Description: This method is called for a new employee. If the employee exists in the
EmpBasic table the data will be defaulted in the PREmployee record.
   OperationID: GetShopEmployeeInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShopEmployeeInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShopEmployeeInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetShopEmployeeInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/GetShopEmployeeInfo", {
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
   Summary: Invoke method RemoveEmployeeResultsLinkCompany
   Description: This method will add employee results link to all employees in the company
   OperationID: RemoveEmployeeResultsLinkCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveEmployeeResultsLinkCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveEmployeeResultsLinkCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveEmployeeResultsLinkCompany(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/RemoveEmployeeResultsLinkCompany", {
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
   Summary: Invoke method ValidateRequiredFields
   Description: Purpose: This method will validate that all required fields have valid data before activate an Employee
<param name="ds">PREmploye Entry data set</param>
   OperationID: ValidateRequiredFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateRequiredFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRequiredFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateRequiredFields(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/ValidateRequiredFields", {
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
   Summary: Invoke method ValidatePayRate
   Description: Purpose: This method will validate that a rate has not a duplicated rateDate for an employee
<param name="empLink">empLink field in PREmpRt</param><param name="rateDate">rateDate field in PREmpRt</param>
   OperationID: ValidatePayRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePayRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePayRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePayRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/ValidatePayRate", {
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
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/GetCodeDescList", {
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
   Summary: Invoke method ModifySearchIDs
   Description: Modify Search ID.
   OperationID: ModifySearchIDs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ModifySearchIDs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ModifySearchIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ModifySearchIDs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/ModifySearchIDs", {
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
   Summary: Invoke method GetNewPREmpMas
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPREmpMas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPREmpMas_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPREmpMas_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPREmpMas(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/GetNewPREmpMas", {
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
   Summary: Invoke method GetNewPREmpMasAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPREmpMasAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPREmpMasAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPREmpMasAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPREmpMasAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/GetNewPREmpMasAttch", {
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
   Summary: Invoke method GetNewPREmpDed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPREmpDed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPREmpDed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPREmpDed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPREmpDed(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/GetNewPREmpDed", {
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
   Summary: Invoke method GetNewPREmpRt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPREmpRt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPREmpRt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPREmpRt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPREmpRt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/GetNewPREmpRt", {
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
   Summary: Invoke method GetNewPREmpTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPREmpTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPREmpTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPREmpTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPREmpTax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/GetNewPREmpTax", {
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
   Summary: Invoke method GetNewEntityGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEntityGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEntityGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEntityGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEntityGLC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/GetNewEntityGLC", {
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
   Summary: Invoke method GetNewPartner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/GetNewPartner", {
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
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/DeleteByID", {
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
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowID(id:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof id!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "id=" + id
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/GetBySysRowID" + params, {
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

   /**  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowIDs(ids:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof ids!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ids=" + ids
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/GetBySysRowIDs" + params, {
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

   /**  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/Update", {
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
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PREmployeeSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EntityGLCRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpDedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PREmpDedRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpMasAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PREmpMasAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpMasListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PREmpMasListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpMasRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PREmpMasRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpRtRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PREmpRtRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PREmpTaxRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PREmpTaxRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartnerRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartnerRow[],
}

export interface Erp_Tablesets_EntityGLCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  */  
   "Key2":string,
      /**   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key3":string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key4":string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key5":string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key6":string,
      /**  Identifier of the GL Control Type.  */  
   "GLControlType":string,
      /**  GL Control Identifier.  */  
   "GLControlCode":string,
      /**  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  */  
   "BusinessEntity":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   "IsExternalCompany":boolean,
      /**  Marks this EntityGLC as global, available to be sent out to other companies.  */  
   "GlobalEntityGLC":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  BankAcctID of the related BankAcct record.  */  
   "BankAcctID":string,
   "BankFeeID":string,
      /**  CallCode of the related FSCallCd record.  */  
   "CallCode":string,
   "ChargeCode":string,
      /**  ClassCode of the related FAClass record.  */  
   "ClassCode":string,
      /**  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  */  
   "ClassID":string,
      /**  ContractCode of the related FSContCd record.  */  
   "ContractCode":string,
      /**  CurrencyCode of the related Currency record.  */  
   "CurrencyCode":string,
      /**  CustNum of the related Customer record  */  
   "CustNum":number,
      /**  DeductionID of PRClsDed or PRDeduct.  */  
   "DeductionID":string,
      /**  EmpID of the related PREmpMas record.  */  
   "EmpID":string,
      /**  ExpenseCode of PayTLbr, LabExpCd  */  
   "ExpenseCode":string,
      /**  ExtSystemID of ExtCompany table  */  
   "ExtSystemID":string,
      /**  FromPlant value of the related PlntTranDef record.  */  
   "FromPlant":string,
      /**  GroupCode of the related FAGroup record.  */  
   "GroupCode":string,
   "GroupID":string,
   "HeadNum":number,
   "InvoiceNum":string,
      /**  JCDept of the related JCDept record.  */  
   "JCDept":string,
      /**  MiscCode of the related MiscChrg or PurMisc record.  */  
   "MiscCode":string,
      /**  PartNum of the related Part record.  */  
   "PartNum":string,
      /**  PayTypeID of PayType  */  
   "PayTypeID":string,
   "PerConName":string,
      /**  PI Status  */  
   "PIStatus":string,
      /**  Plant of the related PlantConfCtrl record.  */  
   "Plant":string,
      /**  ProdCode of the related ProdGrup record.  */  
   "ProdCode":string,
      /**  ProjectID of the related Project record.  */  
   "ProjectID":string,
      /**  PurchCode of the related GLPurch record.  */  
   "PurchCode":string,
      /**  RateCode of the related GLRate record.  */  
   "RateCode":string,
      /**  ReasonCode of the related Reason record.  */  
   "ReasonCode":string,
      /**  ReasonType of the related Reason record.  */  
   "ReasonType":string,
      /**  SalesCatID of the related SalesCat record.  */  
   "SalesCatID":string,
      /**  Shift value of the related JCShift record.  */  
   "Shift":number,
      /**  TaxCode of the related SalesTax record.  */  
   "TaxCode":string,
      /**  TaxTblID of PRTaxMas or PRClsTax.  */  
   "TaxTblID":string,
      /**  ToPlant value of the related PlntTranDef record.  */  
   "ToPlant":string,
      /**  TransferMethod of ExtCompany table  */  
   "TransferMethod":string,
      /**  Type ID  */  
   "TypeID":string,
      /**  VendorNum of the related Vendor record.  */  
   "VendorNum":number,
      /**  WarehouseCode of the related Warehse record.  */  
   "WarehouseCode":string,
   "ExpenseTypeCode":string,
   "IsFiltered":boolean,
   "OprTypeCode":string,
   "CashDeskID":string,
   "TIN":string,
   "ReclassCodeID":string,
   "BitFlag":number,
   "GLCntrlDescription":string,
   "GLCntrlTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PREmpDedRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  encoded value which identifies the employee.  */  
   "EmpLink":string,
      /**  The ID of the related deduction master  */  
   "DeductionID":string,
      /**  DeductionNum uniquely identifies a PREmpDed record for an employee, for a specific DeductionID.  This enables an employee to have the same Deduction established more than once without having to set up a new deduction master.  For example, you may have a deduction for loan repayments and the employee may have multiple loans each with there own declining balances established.  This integer is assigned by the system automatically by finding the last related records number and adding one to it.  */  
   "DeductionNum":number,
      /**  Indicates that this deduction is taken during deduction period 1. Deduction periods (of which there are five) provide a method of controlling when the deduction is to be taken.  When payroll is run you are asked to enter a deduction period.  Only deductions that have that period marked will be taken. An exception to this rule would be if the CarryOverAmt <> 0 (see CarryOverAmt).  */  
   "Period1":boolean,
      /**  Indicates that this deduction is taken during deduction period 2.  (Also see Period1).  */  
   "Period2":boolean,
      /**  Indicates if this deduction is taken during deduction period 3.  (Also see Period1).  */  
   "Period3":boolean,
      /**  Indicates if this deduction is taken during deduction period 4.  (Also see Period1).  */  
   "Period4":boolean,
      /**  Indicates if this deduction is taken during deduction period 5.  (Also see Period1).  */  
   "Period5":boolean,
      /**  Deduction Rate.  This can represent either a fixed amount or a percent of gross wages (see RateQualifier).  */  
   "Rate":number,
      /**   The value of this field qualifies the value stored in the Rate field as either a fixed amount, percent of gross or percent of net pay. Defaulted from PRDeduct.RateQualifier.
Amt = Amount,  %Grs = Percent of gross, %Net = Percent of Net.
Note:  %Net is not allowed if the deduction is exempt from any taxes (records in PRDedXTx).  if %Net then this deduction is calculated after all other deductions and taxes, regardless of the deduction being tax exempt.  A deduction could be %Net and marked as tax exempt if the deduction was made tax exempt after it had already been marked as %Net.  */  
   "RateQualifier":string,
      /**  This is the original amount of the declining deduction.  It is used primarily as a reference.  */  
   "DeclineOrigAmt":number,
      /**  This is the remaining amount of the declining deduction.  */  
   "DeclineRemAmt":number,
      /**  This value sets a maximum check limit on the amount of this deduction.  */  
   "CheckLimit":number,
      /**  This value sets a maximum monthly limit on the amount of this deduction.  The month is determined by using the check date.  */  
   "MonthLimit":number,
      /**  This value sets a maximum yearly limit on the amount of this deduction.  The year is determined by using the check date.  */  
   "YearlyLimit":number,
      /**  Amount carried over from previous pay period.  The system will attempt to deduct this amount in the very next pay period regardless of the deduction cycle.  */  
   "CarryOverAmt":number,
      /**  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   "ClassID":string,
      /**  Used to indicate the record is inactive. Inactive = Yes prevents the deduction from being taken.  */  
   "InActive":boolean,
      /**  Employee specific information that can be used to further describe the reason for the deduction. For example; you may have a generic deduction called "Purchases", using the reference you could identify what the employee's purchase was. This field is printed on the check stub.  */  
   "Reference":string,
      /**  Comments are intended to be internal comments about a specific deduction.  */  
   "CommentText":string,
      /**  Employee's Bank Routing Number  */  
   "BankRoutingNum":string,
      /**  Employee's Bank Account Number  */  
   "BankAcctNum":string,
      /**  The name the employee's bank account is under.  It doesn't have to match the employee's name.  */  
   "BankAcctName":string,
      /**  The employee's bank account type:  C - Checking, S - Savings, etc.  */  
   "BankAcctType":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "EmpID":string,
   "ElecDeposit":boolean,
   "CarryOver":boolean,
   "DeclineBalance":boolean,
   "BitFlag":number,
   "ClassIDDescription":string,
   "DeductionDescription":string,
   "DeductionHCMLinked":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PREmpMasAttchRow{
   "Company":string,
   "EmpID":string,
   "DrawingSeq":number,
   "XFileRefNum":number,
   "SysRevID":number,
   "SysRowID":string,
   "ForeignSysRowID":string,
   "DrawDesc":string,
   "FileName":string,
   "PDMDocID":string,
   "DocTypeID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PREmpMasListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Employee ID.  */  
   "EmpID":string,
      /**  Encrypted Social security number.  */  
   "SocSecNum":string,
      /**  First name of employee.  */  
   "FirstName":string,
      /**  Middle name of employee.  */  
   "MiddleInitial":string,
      /**  Last name of employee  */  
   "LastName":string,
      /**  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   "Name":string,
      /**  First Address line  */  
   "Address":string,
      /**  Second Address line  */  
   "Address2":string,
      /**  City portion of the address  */  
   "City":string,
      /**  Home State. Can be blank.  */  
   "State":string,
      /**  Postal code or zip code portion of the address  */  
   "ZIP":string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   "Country":string,
      /**  Home phone number  */  
   "Phone":string,
      /**   Payroll class ID that employee is assigned to. This is MANDATORY and must be valid in the PRClass table
(See PRClass table)  */  
   "ClassID":string,
      /**  Normal work shift.  */  
   "Shift":number,
      /**  Date that employee was hired.  */  
   "HireDate":string,
      /**  Indicates if employee has been terminated.  */  
   "Terminated":boolean,
      /**  Date that employee was terminated from employment.  */  
   "TerminatedDate":string,
      /**  H = Hourly,  S = Salaried.  */  
   "PayType":string,
      /**  How often the employee is paid. Valid values are  "Weekly", "Biweekly", Semimonthly, and "Monthly"  */  
   "PayFrequency":string,
      /**  Indicates if this an active shop employee. This controls the creation of EmpBasic record from PREmpDat.  If this is Yes, then during the write trigger the EmpBasic record will be created.  If this is "No" and EmpBasic exists then EmpBasic is deleted if there is no related LaborDtl records, else it is set "EmpBasic.EmpStatus = "I"".   If it is set to true then the empbasic record is created and the EmpBasic.EmpStatus field is set to "A".  */  
   "ShopEmployee":boolean,
      /**   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  */  
   "SupervisorID":string,
      /**  Email address of the payroll employee.  */  
   "EMailAddress":string,
      /**   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  */  
   "DcdUserID":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Unencrypted Social Security Number for input and display purposes.  */  
   "DspSocSecNum":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PREmpMasRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Employee ID.  */  
   "EmpID":string,
      /**  Encoded value for employee which can be used to link the PREmpMas with it's sub related files.  This field is normally blank, which means file joins are impossible. This value can be set/reset only by the payroll manager via an option in system maintenance.  */  
   "EmpLink":string,
      /**  Encrypted Social security number.  */  
   "SocSecNum":string,
      /**  First name of employee.  */  
   "FirstName":string,
      /**  Middle name of employee.  */  
   "MiddleInitial":string,
      /**  Last name of employee  */  
   "LastName":string,
      /**  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   "Name":string,
      /**  First Address line  */  
   "Address":string,
      /**  Second Address line  */  
   "Address2":string,
      /**  City portion of the address  */  
   "City":string,
      /**  Home State. Can be blank.  */  
   "State":string,
      /**  Postal code or zip code portion of the address  */  
   "ZIP":string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   "Country":string,
      /**  Home phone number  */  
   "Phone":string,
      /**  Emergency Phone number  */  
   "EmgPhone":string,
      /**  Emergency contact name.  */  
   "EmgContact":string,
      /**   Payroll class ID that employee is assigned to. This is MANDATORY and must be valid in the PRClass table
(See PRClass table)  */  
   "ClassID":string,
      /**  Normal work shift.  */  
   "Shift":number,
      /**  Labor rate that is used for Job Costing.  */  
   "LaborRate":number,
      /**   The default expense code that will be for direct labor hours reported by this employee.  This must be valid in the LabExpCd master file.
This will be used unless labor is reported where the JobHead.ExpenseCode is not blank.  */  
   "ExpenseCode":string,
      /**   The Job Department in which the employee works work was done. An optional field. If entered must be valid in JCDept table.
Used by data collection in the "Work Que" window to provide a default department to view.  */  
   "JCDept":string,
      /**  Date that employee was hired.  */  
   "HireDate":string,
      /**  Indicates if employee has been terminated.  */  
   "Terminated":boolean,
      /**  Date that employee was terminated from employment.  */  
   "TerminatedDate":string,
      /**  Employees birthday  */  
   "BirthDate":string,
      /**  H = Hourly,  S = Salaried.  */  
   "PayType":string,
      /**  How often the employee is paid. Valid values are  "Weekly", "Biweekly", Semimonthly, and "Monthly"  */  
   "PayFrequency":string,
      /**  Indicates if this employee is part of a pension plan.  This is used to print on the W2 form  */  
   "Pension":boolean,
      /**  Indicates if this employee is part of a deferred compensation plan.  This is used to print on the W2 form  */  
   "DeferredComp":boolean,
      /**  The workman's compensation master that this employee is related to.  */  
   "WorkCompCode":string,
      /**  The number of hours of vacation time that is earned per pay period.  */  
   "VacAccrualRate":number,
      /**  Vacation hours remaining. This field can be updated through master maintenance.  It is increased by the VacAccuralRate value for each period the employee is paid. It is reduced when vacation hours are entered in check entry.  */  
   "VacRemaining":number,
      /**  Maximum number of vacation hours that can be accrued.  */  
   "VacHrsMax":number,
      /**  The number of hours of sick time that is earned per pay period.  */  
   "SickAccrualRate":number,
      /**  Total Sick hours remaining.  This field can be directly maintained via employee master maintenance.  It gets increased by the SickAccrualRate value for each period an employee gets paid in.  It is decreased by entering Sick Pay hours in check entry.  */  
   "SickRemaining":number,
      /**  Maximum number of sick hours that can be accrued.  */  
   "SickHrsMax":number,
      /**  The override G/L Division for  G/L transactions created by payroll.   This can be left blank or must be valid in the GLDiv master.  The system attempts to use this in the construction of a G/L account number.  The system replaces the division and department components of the account from the appropriate master file (PayType, PRDeduc,  PRTaxMas...) with the PrEmpDat.Division/GlDept if they are non blank. If this combination yields a valid GL account (found in GLAcct and Active = yes) then it is used, else the original account defined by the master is  used. Note: Hours that are transferred from job costing uses the Division/GlDept overrides defined in the JCDept master to override the account defined in the PayType master.  */  
   "Division":string,
      /**  The G/L Department default for payments made in this department.  This can be blank or must be valid in the GLDept master.  This is similar to the PREmpDat.Division, see that fields description for info about how the system creates default G/L accounts.  */  
   "GLDept":string,
      /**  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  */  
   "PhotoFile":string,
      /**  Indicates if this an active shop employee. This controls the creation of EmpBasic record from PREmpDat.  If this is Yes, then during the write trigger the EmpBasic record will be created.  If this is "No" and EmpBasic exists then EmpBasic is deleted if there is no related LaborDtl records, else it is set "EmpBasic.EmpStatus = "I"".   If it is set to true then the empbasic record is created and the EmpBasic.EmpStatus field is set to "A".  */  
   "ShopEmployee":boolean,
      /**  Overtime Threshold Day  */  
   "OTDay":number,
      /**  Overtime Threshold Week  */  
   "OTWeek":number,
      /**   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  */  
   "SupervisorID":string,
      /**  Comments are intended to be internal comments about a specific employee. To be view-as EDITOR widget.  */  
   "CommentText":string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  This person usually goes out on service calls  */  
   "ServTech":boolean,
      /**  Email address of the payroll employee.  */  
   "EMailAddress":string,
      /**   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  */  
   "DcdUserID":string,
      /**  Indicates if this employee works on the manufacturing line. This must be checked for employee to use the Shop Floor Menu production options.  */  
   "ProductionWorker":boolean,
      /**  Indicates if this employee is a material handler. This must be checked for employee to use the Shop Floor Menu material handler options.  */  
   "MaterialHandler":boolean,
      /**  Indicates if this employee is a shop supervisor. This must be checked for employee to use the Shop Floor Menu Supervisor options.  */  
   "ShopSupervisor":boolean,
      /**   Pertains to Data Collection only.
Indicates if the employee is allowed report completed quantities.  */  
   "CanReportQty":boolean,
      /**   Pertains to Data Collection only.
Indicates if the job/asm/opr can be overriden when reporting completed quantity.  If NO, then they will only be allowed to report against a job/asm/opr that they are currently working on (active labordtl record ) or where the job is open and the operation is marked as "quantity only" reporting .  If YES, they can enter the quantity for any open job without first having to do a start activity function.
( See also PREmpMas.CanReportQty )  */  
   "CanOverrideJob":boolean,
      /**   Pertains to Data Collection/Advanced Material Management only.
Indicates if the employee is allowed make requests for materials.  */  
   "CanRequestMaterial":boolean,
      /**   Pertains to Data Collection only.
Indicates if the employee is allowed report scrap quantities.  */  
   "CanReportScrapQty":boolean,
      /**   Pertains to Data Collection only.
Indicates if the employee is allowed report nonconformance quantities.  */  
   "CanReportNCQty":boolean,
      /**  Indicates if this employee is a Shipping/Receiving worker. This must be checked for employee to use the Shop Floor Menu Shipping/Receiving options.  */  
   "ShipRecv":boolean,
      /**  Indicates if there is third part sick pay for W2.  */  
   "ThirdPartySickPay":boolean,
      /**  Indicates a retirement plan for W2.  */  
   "RetirePlan":boolean,
      /**  Unique identifier for an external interface.  */  
   "ExternalID":string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "CnvEmpID":string,
      /**  A warehouse manager has the access to the Manager's Queue tab in the Material Request Queue.  */  
   "WarehouseManager":boolean,
      /**  Employee is able to override a hard allocation against inventory to release it for another Sales Order, Job or Transfer Order during the process of picking and packing orders.  */  
   "CanOverrideAllocations":boolean,
      /**  Unique identifier for a PerCon record.  */  
   "PerConID":number,
      /**  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  */  
   "SyncNameToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  */  
   "SyncAddressToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  */  
   "SyncPhoneToPerCon":boolean,
      /**  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  */  
   "SyncEmailToPerCon":boolean,
      /**  Indicates if the record is linked from HCM  */  
   "HCMLinked":boolean,
      /**  Indicates if the Employee is inactive  */  
   "InActive":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ImageID  */  
   "ImageID":string,
      /**  Path of photo id  */  
   "ImageFile":string,
   "PerConName":string,
      /**  Supervisor Name  */  
   "SupervisorName":string,
      /**  Unencrypted Social Security Number for input and display purposes.  */  
   "DspSocSecNum":string,
   "BitFlag":number,
   "ClassIDDescription":string,
   "CountryNumDescription":string,
   "DcdUserIDName":string,
   "ExpenseDescription":string,
   "JCDeptDescription":string,
   "ShiftDescription":string,
   "UserCompName":string,
   "WorkCompCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PREmpRtRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  encoded value which identifies the employee.  */  
   "EmpLink":string,
      /**  Date at which the current PayRate became effective.  */  
   "RateDate":string,
      /**  Hourly Pay Rate that is used in calculating the pay check amount.  */  
   "PayRate":number,
      /**  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   "ClassID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Employee ID  */  
   "EmpID":string,
   "Salary":number,
   "BitFlag":number,
   "ClassIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PREmpTaxRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Encoded value which identifies the employee.  */  
   "EmpLink":string,
      /**  Identifies the tax master (PRTaxMas) that this EmpTax record is related to.  */  
   "TaxTblID":string,
      /**  Number of personal exemptions that this employee is claiming for this tax.  */  
   "PerExempt":number,
      /**  Number of dependent exemptions that this employee is claiming for this tax.  */  
   "DepExempt":number,
      /**  The tax filing status the employee claims for this tax. Using the TaxTblID and FileStatus must be valid in the PRTaxDtl file.  Examples would be S - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  */  
   "FileStatus":string,
      /**  Additional withholding amount.  */  
   "AddlWithholding":number,
      /**  Annual tax credit amount.  Normally the annual tax credit is calculated by the system as the # of personal/dependent exemptions multiplied by the credit value defined in the tax table. This value is to override that calculation and should only be used in unusual cases where the standard formula does not yield a proper amount.  */  
   "CreditAmount":number,
      /**  Fixed annual exemption amount.  Normally the annual exemption amount is calculated by the system as the # of personal/dependent exemptions multiplied by the exemption value defined in the tax table.  The FixedEX field is used to override that calculation and should only be used in unusual cases where the standard formula does not yield a proper amount.  */  
   "FixedEX":number,
      /**  Indicates that this employee is exempt from this tax.  This is used when an employee needs to be reported for taxes but should not have an actual tax calculated.  This is different than not setting up this tax for the employee in the first place.  */  
   "Exempt":boolean,
      /**  Used to indicate the record is inactive. Inactive = Yes prevents the tax from being taken.  */  
   "InActive":boolean,
      /**  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   "ClassID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "EmpID":string,
      /**  From PRTaxDtl.FileStatus  */  
   "TaxDetailFileStatusDesc":string,
   "BitFlag":number,
   "ClassIDDescription":string,
   "TaxMasterDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartnerRow{
      /**  Company  */  
   "Company":string,
      /**  PartnerNum  */  
   "PartnerNum":number,
      /**  PartnerType  */  
   "PartnerType":number,
      /**  SearchID  */  
   "SearchID":string,
      /**  IsActive  */  
   "IsActive":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  PartnerID  */  
   "PartnerID":string,
   "DspSearchID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ds
   */  
export interface AddEmployeeResultsLinkCompany_input{
   ds:Erp_Tablesets_PREmployeeTableset[],
}

export interface AddEmployeeResultsLinkCompany_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PREmployeeTableset[],
   opMessage:string,
}
}

export interface BuildClassList_output{
parameters : {
      /**  output parameters  */  
   classList:string,
}
}

   /** Required : 
      @param taxTblID
   */  
export interface BuildFilingList_input{
      /**  Tax Table ID code  */  
   taxTblID:string,
}

export interface BuildFilingList_output{
parameters : {
      /**  output parameters  */  
   filingList:string,
}
}

   /** Required : 
      @param taxTblID
      @param empID
   */  
export interface BuildTaxTblList_input{
      /**  Current Tax Table ID, blank if new  */  
   taxTblID:string,
      /**  Curreny Employee ID  */  
   empID:string,
}

export interface BuildTaxTblList_output{
parameters : {
      /**  output parameters  */  
   taxList:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CalcSalaryRate_input{
   ds:Erp_Tablesets_PREmployeeTableset[],
}

export interface CalcSalaryRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PREmployeeTableset[],
}
}

   /** Required : 
      @param ProposedFileStatus
      @param ds
   */  
export interface ChangeFileStatus_input{
      /**  propsed value  */  
   ProposedFileStatus:string,
   ds:Erp_Tablesets_PREmployeeTableset[],
}

export interface ChangeFileStatus_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PREmployeeTableset[],
}
}

   /** Required : 
      @param jcDept
   */  
export interface CheckJCDeptExists_input{
      /**  Job department to validate.  */  
   jcDept:string,
}

export interface CheckJCDeptExists_output{
   returnObj:boolean,
}

   /** Required : 
      @param labExpCode
   */  
export interface CheckLaborExpCodeExists_input{
      /**  Labor expense code to validate.  */  
   labExpCode:string,
}

export interface CheckLaborExpCodeExists_output{
   returnObj:boolean,
}

   /** Required : 
      @param empId
   */  
export interface CheckLeavePREmpMas_input{
      /**  The current employee's ID  */  
   empId:string,
}

export interface CheckLeavePREmpMas_output{
parameters : {
      /**  output parameters  */  
   vMessage:string,
}
}

   /** Required : 
      @param classID
   */  
export interface CheckPRClassExisst_input{
      /**  Class to validate.  */  
   classID:string,
}

export interface CheckPRClassExisst_output{
   returnObj:boolean,
}

   /** Required : 
      @param workCompCode
   */  
export interface CheckPRWorkCompCodeExists_input{
      /**  Worker's compensation code to validate.  */  
   workCompCode:string,
}

export interface CheckPRWorkCompCodeExists_output{
   returnObj:boolean,
}

   /** Required : 
      @param PayRateDate
      @param PREmpID
      @param PRRateSysRowID
   */  
export interface CheckPayRateEffectiveDate_input{
      /**  the pay rate date  */  
   PayRateDate:string,
      /**  the payroll employee id  */  
   PREmpID:string,
      /**  the PREmpRt SysRowID  */  
   PRRateSysRowID:string,
}

export interface CheckPayRateEffectiveDate_output{
parameters : {
      /**  output parameters  */  
   OutMessageText:string,
}
}

   /** Required : 
      @param PerConID
      @param EmpID
   */  
export interface CheckPersonContact_input{
      /**  The Person Contact ID  */  
   PerConID:number,
      /**  ID of the current Employee  */  
   EmpID:string,
}

export interface CheckPersonContact_output{
parameters : {
      /**  output parameters  */  
   OutMessageText:string,
}
}

   /** Required : 
      @param empID
   */  
export interface DeleteByID_input{
   empID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_EntityGLCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  */  
   Key2:string,
      /**   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key3:string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key4:string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key5:string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key6:string,
      /**  Identifier of the GL Control Type.  */  
   GLControlType:string,
      /**  GL Control Identifier.  */  
   GLControlCode:string,
      /**  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  */  
   BusinessEntity:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   IsExternalCompany:boolean,
      /**  Marks this EntityGLC as global, available to be sent out to other companies.  */  
   GlobalEntityGLC:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BankAcctID of the related BankAcct record.  */  
   BankAcctID:string,
   BankFeeID:string,
      /**  CallCode of the related FSCallCd record.  */  
   CallCode:string,
   ChargeCode:string,
      /**  ClassCode of the related FAClass record.  */  
   ClassCode:string,
      /**  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  */  
   ClassID:string,
      /**  ContractCode of the related FSContCd record.  */  
   ContractCode:string,
      /**  CurrencyCode of the related Currency record.  */  
   CurrencyCode:string,
      /**  CustNum of the related Customer record  */  
   CustNum:number,
      /**  DeductionID of PRClsDed or PRDeduct.  */  
   DeductionID:string,
      /**  EmpID of the related PREmpMas record.  */  
   EmpID:string,
      /**  ExpenseCode of PayTLbr, LabExpCd  */  
   ExpenseCode:string,
      /**  ExtSystemID of ExtCompany table  */  
   ExtSystemID:string,
      /**  FromPlant value of the related PlntTranDef record.  */  
   FromPlant:string,
      /**  GroupCode of the related FAGroup record.  */  
   GroupCode:string,
   GroupID:string,
   HeadNum:number,
   InvoiceNum:string,
      /**  JCDept of the related JCDept record.  */  
   JCDept:string,
      /**  MiscCode of the related MiscChrg or PurMisc record.  */  
   MiscCode:string,
      /**  PartNum of the related Part record.  */  
   PartNum:string,
      /**  PayTypeID of PayType  */  
   PayTypeID:string,
   PerConName:string,
      /**  PI Status  */  
   PIStatus:string,
      /**  Plant of the related PlantConfCtrl record.  */  
   Plant:string,
      /**  ProdCode of the related ProdGrup record.  */  
   ProdCode:string,
      /**  ProjectID of the related Project record.  */  
   ProjectID:string,
      /**  PurchCode of the related GLPurch record.  */  
   PurchCode:string,
      /**  RateCode of the related GLRate record.  */  
   RateCode:string,
      /**  ReasonCode of the related Reason record.  */  
   ReasonCode:string,
      /**  ReasonType of the related Reason record.  */  
   ReasonType:string,
      /**  SalesCatID of the related SalesCat record.  */  
   SalesCatID:string,
      /**  Shift value of the related JCShift record.  */  
   Shift:number,
      /**  TaxCode of the related SalesTax record.  */  
   TaxCode:string,
      /**  TaxTblID of PRTaxMas or PRClsTax.  */  
   TaxTblID:string,
      /**  ToPlant value of the related PlntTranDef record.  */  
   ToPlant:string,
      /**  TransferMethod of ExtCompany table  */  
   TransferMethod:string,
      /**  Type ID  */  
   TypeID:string,
      /**  VendorNum of the related Vendor record.  */  
   VendorNum:number,
      /**  WarehouseCode of the related Warehse record.  */  
   WarehouseCode:string,
   ExpenseTypeCode:string,
   IsFiltered:boolean,
   OprTypeCode:string,
   CashDeskID:string,
   TIN:string,
   ReclassCodeID:string,
   BitFlag:number,
   GLCntrlDescription:string,
   GLCntrlTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PREmpDedRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  encoded value which identifies the employee.  */  
   EmpLink:string,
      /**  The ID of the related deduction master  */  
   DeductionID:string,
      /**  DeductionNum uniquely identifies a PREmpDed record for an employee, for a specific DeductionID.  This enables an employee to have the same Deduction established more than once without having to set up a new deduction master.  For example, you may have a deduction for loan repayments and the employee may have multiple loans each with there own declining balances established.  This integer is assigned by the system automatically by finding the last related records number and adding one to it.  */  
   DeductionNum:number,
      /**  Indicates that this deduction is taken during deduction period 1. Deduction periods (of which there are five) provide a method of controlling when the deduction is to be taken.  When payroll is run you are asked to enter a deduction period.  Only deductions that have that period marked will be taken. An exception to this rule would be if the CarryOverAmt <> 0 (see CarryOverAmt).  */  
   Period1:boolean,
      /**  Indicates that this deduction is taken during deduction period 2.  (Also see Period1).  */  
   Period2:boolean,
      /**  Indicates if this deduction is taken during deduction period 3.  (Also see Period1).  */  
   Period3:boolean,
      /**  Indicates if this deduction is taken during deduction period 4.  (Also see Period1).  */  
   Period4:boolean,
      /**  Indicates if this deduction is taken during deduction period 5.  (Also see Period1).  */  
   Period5:boolean,
      /**  Deduction Rate.  This can represent either a fixed amount or a percent of gross wages (see RateQualifier).  */  
   Rate:number,
      /**   The value of this field qualifies the value stored in the Rate field as either a fixed amount, percent of gross or percent of net pay. Defaulted from PRDeduct.RateQualifier.
Amt = Amount,  %Grs = Percent of gross, %Net = Percent of Net.
Note:  %Net is not allowed if the deduction is exempt from any taxes (records in PRDedXTx).  if %Net then this deduction is calculated after all other deductions and taxes, regardless of the deduction being tax exempt.  A deduction could be %Net and marked as tax exempt if the deduction was made tax exempt after it had already been marked as %Net.  */  
   RateQualifier:string,
      /**  This is the original amount of the declining deduction.  It is used primarily as a reference.  */  
   DeclineOrigAmt:number,
      /**  This is the remaining amount of the declining deduction.  */  
   DeclineRemAmt:number,
      /**  This value sets a maximum check limit on the amount of this deduction.  */  
   CheckLimit:number,
      /**  This value sets a maximum monthly limit on the amount of this deduction.  The month is determined by using the check date.  */  
   MonthLimit:number,
      /**  This value sets a maximum yearly limit on the amount of this deduction.  The year is determined by using the check date.  */  
   YearlyLimit:number,
      /**  Amount carried over from previous pay period.  The system will attempt to deduct this amount in the very next pay period regardless of the deduction cycle.  */  
   CarryOverAmt:number,
      /**  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   ClassID:string,
      /**  Used to indicate the record is inactive. Inactive = Yes prevents the deduction from being taken.  */  
   InActive:boolean,
      /**  Employee specific information that can be used to further describe the reason for the deduction. For example; you may have a generic deduction called "Purchases", using the reference you could identify what the employee's purchase was. This field is printed on the check stub.  */  
   Reference:string,
      /**  Comments are intended to be internal comments about a specific deduction.  */  
   CommentText:string,
      /**  Employee's Bank Routing Number  */  
   BankRoutingNum:string,
      /**  Employee's Bank Account Number  */  
   BankAcctNum:string,
      /**  The name the employee's bank account is under.  It doesn't have to match the employee's name.  */  
   BankAcctName:string,
      /**  The employee's bank account type:  C - Checking, S - Savings, etc.  */  
   BankAcctType:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   EmpID:string,
   ElecDeposit:boolean,
   CarryOver:boolean,
   DeclineBalance:boolean,
   BitFlag:number,
   ClassIDDescription:string,
   DeductionDescription:string,
   DeductionHCMLinked:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PREmpMasAttchRow{
   Company:string,
   EmpID:string,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PREmpMasListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Employee ID.  */  
   EmpID:string,
      /**  Encrypted Social security number.  */  
   SocSecNum:string,
      /**  First name of employee.  */  
   FirstName:string,
      /**  Middle name of employee.  */  
   MiddleInitial:string,
      /**  Last name of employee  */  
   LastName:string,
      /**  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   Name:string,
      /**  First Address line  */  
   Address:string,
      /**  Second Address line  */  
   Address2:string,
      /**  City portion of the address  */  
   City:string,
      /**  Home State. Can be blank.  */  
   State:string,
      /**  Postal code or zip code portion of the address  */  
   ZIP:string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   Country:string,
      /**  Home phone number  */  
   Phone:string,
      /**   Payroll class ID that employee is assigned to. This is MANDATORY and must be valid in the PRClass table
(See PRClass table)  */  
   ClassID:string,
      /**  Normal work shift.  */  
   Shift:number,
      /**  Date that employee was hired.  */  
   HireDate:string,
      /**  Indicates if employee has been terminated.  */  
   Terminated:boolean,
      /**  Date that employee was terminated from employment.  */  
   TerminatedDate:string,
      /**  H = Hourly,  S = Salaried.  */  
   PayType:string,
      /**  How often the employee is paid. Valid values are  "Weekly", "Biweekly", Semimonthly, and "Monthly"  */  
   PayFrequency:string,
      /**  Indicates if this an active shop employee. This controls the creation of EmpBasic record from PREmpDat.  If this is Yes, then during the write trigger the EmpBasic record will be created.  If this is "No" and EmpBasic exists then EmpBasic is deleted if there is no related LaborDtl records, else it is set "EmpBasic.EmpStatus = "I"".   If it is set to true then the empbasic record is created and the EmpBasic.EmpStatus field is set to "A".  */  
   ShopEmployee:boolean,
      /**   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  */  
   SupervisorID:string,
      /**  Email address of the payroll employee.  */  
   EMailAddress:string,
      /**   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  */  
   DcdUserID:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Unencrypted Social Security Number for input and display purposes.  */  
   DspSocSecNum:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PREmpMasListTableset{
   PREmpMasList:Erp_Tablesets_PREmpMasListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PREmpMasRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Employee ID.  */  
   EmpID:string,
      /**  Encoded value for employee which can be used to link the PREmpMas with it's sub related files.  This field is normally blank, which means file joins are impossible. This value can be set/reset only by the payroll manager via an option in system maintenance.  */  
   EmpLink:string,
      /**  Encrypted Social security number.  */  
   SocSecNum:string,
      /**  First name of employee.  */  
   FirstName:string,
      /**  Middle name of employee.  */  
   MiddleInitial:string,
      /**  Last name of employee  */  
   LastName:string,
      /**  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   Name:string,
      /**  First Address line  */  
   Address:string,
      /**  Second Address line  */  
   Address2:string,
      /**  City portion of the address  */  
   City:string,
      /**  Home State. Can be blank.  */  
   State:string,
      /**  Postal code or zip code portion of the address  */  
   ZIP:string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   Country:string,
      /**  Home phone number  */  
   Phone:string,
      /**  Emergency Phone number  */  
   EmgPhone:string,
      /**  Emergency contact name.  */  
   EmgContact:string,
      /**   Payroll class ID that employee is assigned to. This is MANDATORY and must be valid in the PRClass table
(See PRClass table)  */  
   ClassID:string,
      /**  Normal work shift.  */  
   Shift:number,
      /**  Labor rate that is used for Job Costing.  */  
   LaborRate:number,
      /**   The default expense code that will be for direct labor hours reported by this employee.  This must be valid in the LabExpCd master file.
This will be used unless labor is reported where the JobHead.ExpenseCode is not blank.  */  
   ExpenseCode:string,
      /**   The Job Department in which the employee works work was done. An optional field. If entered must be valid in JCDept table.
Used by data collection in the "Work Que" window to provide a default department to view.  */  
   JCDept:string,
      /**  Date that employee was hired.  */  
   HireDate:string,
      /**  Indicates if employee has been terminated.  */  
   Terminated:boolean,
      /**  Date that employee was terminated from employment.  */  
   TerminatedDate:string,
      /**  Employees birthday  */  
   BirthDate:string,
      /**  H = Hourly,  S = Salaried.  */  
   PayType:string,
      /**  How often the employee is paid. Valid values are  "Weekly", "Biweekly", Semimonthly, and "Monthly"  */  
   PayFrequency:string,
      /**  Indicates if this employee is part of a pension plan.  This is used to print on the W2 form  */  
   Pension:boolean,
      /**  Indicates if this employee is part of a deferred compensation plan.  This is used to print on the W2 form  */  
   DeferredComp:boolean,
      /**  The workman's compensation master that this employee is related to.  */  
   WorkCompCode:string,
      /**  The number of hours of vacation time that is earned per pay period.  */  
   VacAccrualRate:number,
      /**  Vacation hours remaining. This field can be updated through master maintenance.  It is increased by the VacAccuralRate value for each period the employee is paid. It is reduced when vacation hours are entered in check entry.  */  
   VacRemaining:number,
      /**  Maximum number of vacation hours that can be accrued.  */  
   VacHrsMax:number,
      /**  The number of hours of sick time that is earned per pay period.  */  
   SickAccrualRate:number,
      /**  Total Sick hours remaining.  This field can be directly maintained via employee master maintenance.  It gets increased by the SickAccrualRate value for each period an employee gets paid in.  It is decreased by entering Sick Pay hours in check entry.  */  
   SickRemaining:number,
      /**  Maximum number of sick hours that can be accrued.  */  
   SickHrsMax:number,
      /**  The override G/L Division for  G/L transactions created by payroll.   This can be left blank or must be valid in the GLDiv master.  The system attempts to use this in the construction of a G/L account number.  The system replaces the division and department components of the account from the appropriate master file (PayType, PRDeduc,  PRTaxMas...) with the PrEmpDat.Division/GlDept if they are non blank. If this combination yields a valid GL account (found in GLAcct and Active = yes) then it is used, else the original account defined by the master is  used. Note: Hours that are transferred from job costing uses the Division/GlDept overrides defined in the JCDept master to override the account defined in the PayType master.  */  
   Division:string,
      /**  The G/L Department default for payments made in this department.  This can be blank or must be valid in the GLDept master.  This is similar to the PREmpDat.Division, see that fields description for info about how the system creates default G/L accounts.  */  
   GLDept:string,
      /**  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  */  
   PhotoFile:string,
      /**  Indicates if this an active shop employee. This controls the creation of EmpBasic record from PREmpDat.  If this is Yes, then during the write trigger the EmpBasic record will be created.  If this is "No" and EmpBasic exists then EmpBasic is deleted if there is no related LaborDtl records, else it is set "EmpBasic.EmpStatus = "I"".   If it is set to true then the empbasic record is created and the EmpBasic.EmpStatus field is set to "A".  */  
   ShopEmployee:boolean,
      /**  Overtime Threshold Day  */  
   OTDay:number,
      /**  Overtime Threshold Week  */  
   OTWeek:number,
      /**   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  */  
   SupervisorID:string,
      /**  Comments are intended to be internal comments about a specific employee. To be view-as EDITOR widget.  */  
   CommentText:string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  This person usually goes out on service calls  */  
   ServTech:boolean,
      /**  Email address of the payroll employee.  */  
   EMailAddress:string,
      /**   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  */  
   DcdUserID:string,
      /**  Indicates if this employee works on the manufacturing line. This must be checked for employee to use the Shop Floor Menu production options.  */  
   ProductionWorker:boolean,
      /**  Indicates if this employee is a material handler. This must be checked for employee to use the Shop Floor Menu material handler options.  */  
   MaterialHandler:boolean,
      /**  Indicates if this employee is a shop supervisor. This must be checked for employee to use the Shop Floor Menu Supervisor options.  */  
   ShopSupervisor:boolean,
      /**   Pertains to Data Collection only.
Indicates if the employee is allowed report completed quantities.  */  
   CanReportQty:boolean,
      /**   Pertains to Data Collection only.
Indicates if the job/asm/opr can be overriden when reporting completed quantity.  If NO, then they will only be allowed to report against a job/asm/opr that they are currently working on (active labordtl record ) or where the job is open and the operation is marked as "quantity only" reporting .  If YES, they can enter the quantity for any open job without first having to do a start activity function.
( See also PREmpMas.CanReportQty )  */  
   CanOverrideJob:boolean,
      /**   Pertains to Data Collection/Advanced Material Management only.
Indicates if the employee is allowed make requests for materials.  */  
   CanRequestMaterial:boolean,
      /**   Pertains to Data Collection only.
Indicates if the employee is allowed report scrap quantities.  */  
   CanReportScrapQty:boolean,
      /**   Pertains to Data Collection only.
Indicates if the employee is allowed report nonconformance quantities.  */  
   CanReportNCQty:boolean,
      /**  Indicates if this employee is a Shipping/Receiving worker. This must be checked for employee to use the Shop Floor Menu Shipping/Receiving options.  */  
   ShipRecv:boolean,
      /**  Indicates if there is third part sick pay for W2.  */  
   ThirdPartySickPay:boolean,
      /**  Indicates a retirement plan for W2.  */  
   RetirePlan:boolean,
      /**  Unique identifier for an external interface.  */  
   ExternalID:string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   CnvEmpID:string,
      /**  A warehouse manager has the access to the Manager's Queue tab in the Material Request Queue.  */  
   WarehouseManager:boolean,
      /**  Employee is able to override a hard allocation against inventory to release it for another Sales Order, Job or Transfer Order during the process of picking and packing orders.  */  
   CanOverrideAllocations:boolean,
      /**  Unique identifier for a PerCon record.  */  
   PerConID:number,
      /**  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  */  
   SyncNameToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  */  
   SyncAddressToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  */  
   SyncPhoneToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  */  
   SyncEmailToPerCon:boolean,
      /**  Indicates if the record is linked from HCM  */  
   HCMLinked:boolean,
      /**  Indicates if the Employee is inactive  */  
   InActive:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ImageID  */  
   ImageID:string,
      /**  Path of photo id  */  
   ImageFile:string,
   PerConName:string,
      /**  Supervisor Name  */  
   SupervisorName:string,
      /**  Unencrypted Social Security Number for input and display purposes.  */  
   DspSocSecNum:string,
   BitFlag:number,
   ClassIDDescription:string,
   CountryNumDescription:string,
   DcdUserIDName:string,
   ExpenseDescription:string,
   JCDeptDescription:string,
   ShiftDescription:string,
   UserCompName:string,
   WorkCompCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PREmpRtRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  encoded value which identifies the employee.  */  
   EmpLink:string,
      /**  Date at which the current PayRate became effective.  */  
   RateDate:string,
      /**  Hourly Pay Rate that is used in calculating the pay check amount.  */  
   PayRate:number,
      /**  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   ClassID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Employee ID  */  
   EmpID:string,
   Salary:number,
   BitFlag:number,
   ClassIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PREmpTaxRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Encoded value which identifies the employee.  */  
   EmpLink:string,
      /**  Identifies the tax master (PRTaxMas) that this EmpTax record is related to.  */  
   TaxTblID:string,
      /**  Number of personal exemptions that this employee is claiming for this tax.  */  
   PerExempt:number,
      /**  Number of dependent exemptions that this employee is claiming for this tax.  */  
   DepExempt:number,
      /**  The tax filing status the employee claims for this tax. Using the TaxTblID and FileStatus must be valid in the PRTaxDtl file.  Examples would be S - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  */  
   FileStatus:string,
      /**  Additional withholding amount.  */  
   AddlWithholding:number,
      /**  Annual tax credit amount.  Normally the annual tax credit is calculated by the system as the # of personal/dependent exemptions multiplied by the credit value defined in the tax table. This value is to override that calculation and should only be used in unusual cases where the standard formula does not yield a proper amount.  */  
   CreditAmount:number,
      /**  Fixed annual exemption amount.  Normally the annual exemption amount is calculated by the system as the # of personal/dependent exemptions multiplied by the exemption value defined in the tax table.  The FixedEX field is used to override that calculation and should only be used in unusual cases where the standard formula does not yield a proper amount.  */  
   FixedEX:number,
      /**  Indicates that this employee is exempt from this tax.  This is used when an employee needs to be reported for taxes but should not have an actual tax calculated.  This is different than not setting up this tax for the employee in the first place.  */  
   Exempt:boolean,
      /**  Used to indicate the record is inactive. Inactive = Yes prevents the tax from being taken.  */  
   InActive:boolean,
      /**  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   ClassID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   EmpID:string,
      /**  From PRTaxDtl.FileStatus  */  
   TaxDetailFileStatusDesc:string,
   BitFlag:number,
   ClassIDDescription:string,
   TaxMasterDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PREmployeeTableset{
   PREmpMas:Erp_Tablesets_PREmpMasRow[],
   PREmpMasAttch:Erp_Tablesets_PREmpMasAttchRow[],
   PREmpDed:Erp_Tablesets_PREmpDedRow[],
   PREmpRt:Erp_Tablesets_PREmpRtRow[],
   PREmpTax:Erp_Tablesets_PREmpTaxRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   Partner:Erp_Tablesets_PartnerRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartnerRow{
      /**  Company  */  
   Company:string,
      /**  PartnerNum  */  
   PartnerNum:number,
      /**  PartnerType  */  
   PartnerType:number,
      /**  SearchID  */  
   SearchID:string,
      /**  IsActive  */  
   IsActive:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  PartnerID  */  
   PartnerID:string,
   DspSearchID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtPREmployeeTableset{
   PREmpMas:Erp_Tablesets_PREmpMasRow[],
   PREmpMasAttch:Erp_Tablesets_PREmpMasAttchRow[],
   PREmpDed:Erp_Tablesets_PREmpDedRow[],
   PREmpRt:Erp_Tablesets_PREmpRtRow[],
   PREmpTax:Erp_Tablesets_PREmpTaxRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   Partner:Erp_Tablesets_PartnerRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param empID
   */  
export interface GetByID_input{
   empID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PREmployeeTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PREmployeeTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PREmployeeTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
   tableName:string,
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param ds
   */  
export interface GetDeductDefaults_input{
   ds:Erp_Tablesets_PREmployeeTableset[],
}

export interface GetDeductDefaults_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PREmployeeTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetEmpIDInfo_input{
   ds:Erp_Tablesets_PREmployeeTableset[],
}

export interface GetEmpIDInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PREmployeeTableset[],
}
}

   /** Required : 
      @param inEmpID
   */  
export interface GetEmpLinkValue_input{
      /**  in Employee Link  */  
   inEmpID:string,
}

export interface GetEmpLinkValue_output{
parameters : {
      /**  output parameters  */  
   outEmpLink:string,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_PREmpMasListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param relatedToFile
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param key6
   */  
export interface GetNewEntityGLC_input{
   ds:Erp_Tablesets_PREmployeeTableset[],
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   key6:string,
}

export interface GetNewEntityGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PREmployeeTableset[],
}
}

   /** Required : 
      @param ds
      @param empLink
      @param deductionID
   */  
export interface GetNewPREmpDed_input{
   ds:Erp_Tablesets_PREmployeeTableset[],
   empLink:string,
   deductionID:string,
}

export interface GetNewPREmpDed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PREmployeeTableset[],
}
}

   /** Required : 
      @param ds
      @param empID
   */  
export interface GetNewPREmpMasAttch_input{
   ds:Erp_Tablesets_PREmployeeTableset[],
   empID:string,
}

export interface GetNewPREmpMasAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PREmployeeTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPREmpMas_input{
   ds:Erp_Tablesets_PREmployeeTableset[],
}

export interface GetNewPREmpMas_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PREmployeeTableset[],
}
}

   /** Required : 
      @param ds
      @param empLink
   */  
export interface GetNewPREmpRt_input{
   ds:Erp_Tablesets_PREmployeeTableset[],
   empLink:string,
}

export interface GetNewPREmpRt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PREmployeeTableset[],
}
}

   /** Required : 
      @param ds
      @param empLink
   */  
export interface GetNewPREmpTax_input{
   ds:Erp_Tablesets_PREmployeeTableset[],
   empLink:string,
}

export interface GetNewPREmpTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PREmployeeTableset[],
}
}

   /** Required : 
      @param ds
      @param partnerNum
      @param partnerType
      @param partnerID
   */  
export interface GetNewPartner_input{
   ds:Erp_Tablesets_PREmployeeTableset[],
   partnerNum:number,
   partnerType:number,
   partnerID:string,
}

export interface GetNewPartner_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PREmployeeTableset[],
}
}

   /** Required : 
      @param ds
      @param empID
   */  
export interface GetNewShopEmployee_input{
   ds:Erp_Tablesets_PREmployeeTableset[],
      /**  Shop Employee's ID  */  
   empID:string,
}

export interface GetNewShopEmployee_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PREmployeeTableset[],
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetOverrideList_input{
      /**  The search statement to filter the PREmpMas table on  */  
   whereClause:string,
      /**  The page size (required)  */  
   pageSize:number,
      /**  Absolte Page size (required)  */  
   absolutePage:number,
}

export interface GetOverrideList_output{
   returnObj:Erp_Tablesets_PREmpMasListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param PerConID
      @param ds
   */  
export interface GetPerConData_input{
   PerConID:number,
   ds:Erp_Tablesets_PREmployeeTableset[],
}

export interface GetPerConData_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PREmployeeTableset[],
}
}

   /** Required : 
      @param whereClausePREmpMas
      @param whereClausePREmpMasAttch
      @param whereClausePREmpDed
      @param whereClausePREmpRt
      @param whereClausePREmpTax
      @param whereClauseEntityGLC
      @param whereClausePartner
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePREmpMas:string,
   whereClausePREmpMasAttch:string,
   whereClausePREmpDed:string,
   whereClausePREmpRt:string,
   whereClausePREmpTax:string,
   whereClauseEntityGLC:string,
   whereClausePartner:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PREmployeeTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetShopEmployeeInfo_input{
   ds:Erp_Tablesets_PREmployeeTableset[],
}

export interface GetShopEmployeeInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PREmployeeTableset[],
}
}

export interface Ice_BOUpdErrorRow{
   TableName:string,
   ErrorLevel:string,
   ErrorType:string,
   ErrorText:string,
   ErrorSysRowID:string,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_BOUpdErrorTableset{
   BOUpdError:Ice_BOUpdErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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

   /** Required : 
      @param ds
   */  
export interface ModifySearchIDs_input{
   ds:Erp_Tablesets_PREmployeeTableset[],
}

export interface ModifySearchIDs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PREmployeeTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface RemoveEmployeeResultsLinkCompany_input{
   ds:Erp_Tablesets_PREmployeeTableset[],
}

export interface RemoveEmployeeResultsLinkCompany_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PREmployeeTableset[],
   opMessage:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPREmployeeTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPREmployeeTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PREmployeeTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PREmployeeTableset[],
}
}

   /** Required : 
      @param empLink
      @param rateDate
   */  
export interface ValidatePayRate_input{
   empLink:string,
   rateDate:string,
}

export interface ValidatePayRate_output{
}

   /** Required : 
      @param ds
   */  
export interface ValidateRequiredFields_input{
   ds:Erp_Tablesets_PREmployeeTableset[],
}

export interface ValidateRequiredFields_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PREmployeeTableset[],
}
}

