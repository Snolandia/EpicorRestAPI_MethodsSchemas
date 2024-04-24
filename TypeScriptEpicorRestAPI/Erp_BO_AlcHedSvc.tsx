import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.AlcHedSvc
// Description: class AlcHedSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/$metadata", {
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
   Description: Get AlcHeds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHeds
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHedRow
   */  
export function get_AlcHeds(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHeds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlcHeds(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds", {
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
   Summary: Calls GetByID to retrieve the AlcHed item
   Description: Calls GetByID to retrieve the AlcHed item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHed
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHedRow
   */  
export function get_AlcHeds_Company_AllocID(Company:string, AllocID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlcHed for the service
   Description: Calls UpdateExt to update AlcHed. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHed
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlcHeds_Company_AllocID(Company:string, AllocID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")", {
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
   Summary: Call UpdateExt to delete AlcHed item
   Description: Call UpdateExt to delete AlcHed item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHed
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlcHeds_Company_AllocID(Company:string, AllocID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")", {
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
   Description: Get AlcAccts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcAccts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcAcctRow
   */  
export function get_AlcHeds_Company_AllocID_AlcAccts(Company:string, AllocID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcAccts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AlcAcct item
   Description: Calls GetByID to retrieve the AlcAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcAcct1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param AllocGLAcct Desc: AllocGLAcct   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcAcctRow
   */  
export function get_AlcHeds_Company_AllocID_AlcAccts_Company_AllocID_ParamNbr_AllocGLAcct(Company:string, AllocID:string, ParamNbr:string, AllocGLAcct:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcAccts(" + Company + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get AlcAcctCats items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcAcctCats1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcAcctCatRow
   */  
export function get_AlcHeds_Company_AllocID_AlcAcctCats(Company:string, AllocID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcAcctCatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcAcctCats", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcAcctCatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AlcAcctCat item
   Description: Calls GetByID to retrieve the AlcAcctCat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcAcctCat1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param CategoryID Desc: CategoryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcAcctCatRow
   */  
export function get_AlcHeds_Company_AllocID_AlcAcctCats_Company_AllocID_ParamNbr_CategoryID(Company:string, AllocID:string, ParamNbr:string, CategoryID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcAcctCatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcAcctCats(" + Company + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcAcctCatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get AlcJrnCds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcJrnCds1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcJrnCdRow
   */  
export function get_AlcHeds_Company_AllocID_AlcJrnCds(Company:string, AllocID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcJrnCdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcJrnCds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcJrnCdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AlcJrnCd item
   Description: Calls GetByID to retrieve the AlcJrnCd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcJrnCd1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcJrnCdRow
   */  
export function get_AlcHeds_Company_AllocID_AlcJrnCds_Company_AllocID_ParamNbr_JournalCode(Company:string, AllocID:string, ParamNbr:string, JournalCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcJrnCdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcJrnCds(" + Company + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcJrnCdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get AlcParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcParams1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcParamsRow
   */  
export function get_AlcHeds_Company_AllocID_AlcParams(Company:string, AllocID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcParamsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcParamsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AlcParam item
   Description: Calls GetByID to retrieve the AlcParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcParam1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcParamsRow
   */  
export function get_AlcHeds_Company_AllocID_AlcParams_Company_AllocID_ParamNbr(Company:string, AllocID:string, ParamNbr:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcParamsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcParams(" + Company + "," + AllocID + "," + ParamNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcParamsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get AlcRanges items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcRanges1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcRangeRow
   */  
export function get_AlcHeds_Company_AllocID_AlcRanges(Company:string, AllocID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcRangeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcRanges", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcRangeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AlcRange item
   Description: Calls GetByID to retrieve the AlcRange item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcRange1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcRangeRow
   */  
export function get_AlcHeds_Company_AllocID_AlcRanges_Company_AllocID_ParamNbr_SegmentNbr(Company:string, AllocID:string, ParamNbr:string, SegmentNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcRangeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcRanges(" + Company + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcRangeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get AlcTargets items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcTargets1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcTargetRow
   */  
export function get_AlcHeds_Company_AllocID_AlcTargets(Company:string, AllocID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcTargetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcTargets", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcTargetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AlcTarget item
   Description: Calls GetByID to retrieve the AlcTarget item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcTarget1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param AllocTgtNbr Desc: AllocTgtNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcTargetRow
   */  
export function get_AlcHeds_Company_AllocID_AlcTargets_Company_AllocID_AllocTgtNbr(Company:string, AllocID:string, AllocTgtNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcTargetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcTargets(" + Company + "," + AllocID + "," + AllocTgtNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcTargetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get AlcAccts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcAccts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcAcctRow
   */  
export function get_AlcAccts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcAccts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcAccts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcAcctRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcAcctRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlcAccts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcAccts", {
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
   Summary: Calls GetByID to retrieve the AlcAcct item
   Description: Calls GetByID to retrieve the AlcAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param AllocGLAcct Desc: AllocGLAcct   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcAcctRow
   */  
export function get_AlcAccts_Company_AllocID_ParamNbr_AllocGLAcct(Company:string, AllocID:string, ParamNbr:string, AllocGLAcct:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcAccts(" + Company + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlcAcct for the service
   Description: Calls UpdateExt to update AlcAcct. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param AllocGLAcct Desc: AllocGLAcct   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcAcctRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlcAccts_Company_AllocID_ParamNbr_AllocGLAcct(Company:string, AllocID:string, ParamNbr:string, AllocGLAcct:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcAccts(" + Company + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")", {
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
   Summary: Call UpdateExt to delete AlcAcct item
   Description: Call UpdateExt to delete AlcAcct item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param AllocGLAcct Desc: AllocGLAcct   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlcAccts_Company_AllocID_ParamNbr_AllocGLAcct(Company:string, AllocID:string, ParamNbr:string, AllocGLAcct:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcAccts(" + Company + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")", {
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
   Description: Get AlcAcctCats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcAcctCats
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcAcctCatRow
   */  
export function get_AlcAcctCats(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcAcctCatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcAcctCats", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcAcctCatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcAcctCats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcAcctCatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcAcctCatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlcAcctCats(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcAcctCats", {
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
   Summary: Calls GetByID to retrieve the AlcAcctCat item
   Description: Calls GetByID to retrieve the AlcAcctCat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcAcctCat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param CategoryID Desc: CategoryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcAcctCatRow
   */  
export function get_AlcAcctCats_Company_AllocID_ParamNbr_CategoryID(Company:string, AllocID:string, ParamNbr:string, CategoryID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcAcctCatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcAcctCats(" + Company + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcAcctCatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlcAcctCat for the service
   Description: Calls UpdateExt to update AlcAcctCat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcAcctCat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param CategoryID Desc: CategoryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcAcctCatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlcAcctCats_Company_AllocID_ParamNbr_CategoryID(Company:string, AllocID:string, ParamNbr:string, CategoryID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcAcctCats(" + Company + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")", {
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
   Summary: Call UpdateExt to delete AlcAcctCat item
   Description: Call UpdateExt to delete AlcAcctCat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcAcctCat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param CategoryID Desc: CategoryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlcAcctCats_Company_AllocID_ParamNbr_CategoryID(Company:string, AllocID:string, ParamNbr:string, CategoryID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcAcctCats(" + Company + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")", {
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
   Description: Get AlcJrnCds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcJrnCds
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcJrnCdRow
   */  
export function get_AlcJrnCds(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcJrnCdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcJrnCds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcJrnCdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcJrnCds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcJrnCdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcJrnCdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlcJrnCds(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcJrnCds", {
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
   Summary: Calls GetByID to retrieve the AlcJrnCd item
   Description: Calls GetByID to retrieve the AlcJrnCd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcJrnCd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcJrnCdRow
   */  
export function get_AlcJrnCds_Company_AllocID_ParamNbr_JournalCode(Company:string, AllocID:string, ParamNbr:string, JournalCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcJrnCdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcJrnCds(" + Company + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcJrnCdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlcJrnCd for the service
   Description: Calls UpdateExt to update AlcJrnCd. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcJrnCd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcJrnCdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlcJrnCds_Company_AllocID_ParamNbr_JournalCode(Company:string, AllocID:string, ParamNbr:string, JournalCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcJrnCds(" + Company + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")", {
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
   Summary: Call UpdateExt to delete AlcJrnCd item
   Description: Call UpdateExt to delete AlcJrnCd item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcJrnCd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlcJrnCds_Company_AllocID_ParamNbr_JournalCode(Company:string, AllocID:string, ParamNbr:string, JournalCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcJrnCds(" + Company + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")", {
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
   Description: Get AlcParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcParams
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcParamsRow
   */  
export function get_AlcParams(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcParamsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcParamsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcParamsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcParamsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlcParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParams", {
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
   Summary: Calls GetByID to retrieve the AlcParam item
   Description: Calls GetByID to retrieve the AlcParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcParamsRow
   */  
export function get_AlcParams_Company_AllocID_ParamNbr(Company:string, AllocID:string, ParamNbr:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcParamsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParams(" + Company + "," + AllocID + "," + ParamNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcParamsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlcParam for the service
   Description: Calls UpdateExt to update AlcParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcParamsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlcParams_Company_AllocID_ParamNbr(Company:string, AllocID:string, ParamNbr:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParams(" + Company + "," + AllocID + "," + ParamNbr + ")", {
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
   Summary: Call UpdateExt to delete AlcParam item
   Description: Call UpdateExt to delete AlcParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlcParams_Company_AllocID_ParamNbr(Company:string, AllocID:string, ParamNbr:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParams(" + Company + "," + AllocID + "," + ParamNbr + ")", {
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
   Description: Get AlcNFSrcs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcNFSrcs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcNFSrcRow
   */  
export function get_AlcParams_Company_AllocID_ParamNbr_AlcNFSrcs(Company:string, AllocID:string, ParamNbr:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcNFSrcRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParams(" + Company + "," + AllocID + "," + ParamNbr + ")/AlcNFSrcs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcNFSrcRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AlcNFSrc item
   Description: Calls GetByID to retrieve the AlcNFSrc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcNFSrc1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param SrcSeqNbr Desc: SrcSeqNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcNFSrcRow
   */  
export function get_AlcParams_Company_AllocID_ParamNbr_AlcNFSrcs_Company_AllocID_ParamNbr_SrcSeqNbr(Company:string, AllocID:string, ParamNbr:string, SrcSeqNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcNFSrcRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParams(" + Company + "," + AllocID + "," + ParamNbr + ")/AlcNFSrcs(" + Company + "," + AllocID + "," + ParamNbr + "," + SrcSeqNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcNFSrcRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get AlcParamsBAQs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcParamsBAQs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcParamsBAQRow
   */  
export function get_AlcParams_Company_AllocID_ParamNbr_AlcParamsBAQs(Company:string, AllocID:string, ParamNbr:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcParamsBAQRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParams(" + Company + "," + AllocID + "," + ParamNbr + ")/AlcParamsBAQs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcParamsBAQRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AlcParamsBAQ item
   Description: Calls GetByID to retrieve the AlcParamsBAQ item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcParamsBAQ1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param BAQExportID Desc: BAQExportID   Required: True   Allow empty value : True
      @param BAQParamValNbr Desc: BAQParamValNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcParamsBAQRow
   */  
export function get_AlcParams_Company_AllocID_ParamNbr_AlcParamsBAQs_Company_AllocID_ParamNbr_BAQExportID_BAQParamValNbr(Company:string, AllocID:string, ParamNbr:string, BAQExportID:string, BAQParamValNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcParamsBAQRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParams(" + Company + "," + AllocID + "," + ParamNbr + ")/AlcParamsBAQs(" + Company + "," + AllocID + "," + ParamNbr + "," + BAQExportID + "," + BAQParamValNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcParamsBAQRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get AlcNFSrcs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcNFSrcs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcNFSrcRow
   */  
export function get_AlcNFSrcs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcNFSrcRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcNFSrcs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcNFSrcRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcNFSrcs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcNFSrcRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcNFSrcRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlcNFSrcs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcNFSrcs", {
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
   Summary: Calls GetByID to retrieve the AlcNFSrc item
   Description: Calls GetByID to retrieve the AlcNFSrc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcNFSrc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param SrcSeqNbr Desc: SrcSeqNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcNFSrcRow
   */  
export function get_AlcNFSrcs_Company_AllocID_ParamNbr_SrcSeqNbr(Company:string, AllocID:string, ParamNbr:string, SrcSeqNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcNFSrcRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcNFSrcs(" + Company + "," + AllocID + "," + ParamNbr + "," + SrcSeqNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcNFSrcRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlcNFSrc for the service
   Description: Calls UpdateExt to update AlcNFSrc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcNFSrc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param SrcSeqNbr Desc: SrcSeqNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcNFSrcRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlcNFSrcs_Company_AllocID_ParamNbr_SrcSeqNbr(Company:string, AllocID:string, ParamNbr:string, SrcSeqNbr:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcNFSrcs(" + Company + "," + AllocID + "," + ParamNbr + "," + SrcSeqNbr + ")", {
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
   Summary: Call UpdateExt to delete AlcNFSrc item
   Description: Call UpdateExt to delete AlcNFSrc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcNFSrc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param SrcSeqNbr Desc: SrcSeqNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlcNFSrcs_Company_AllocID_ParamNbr_SrcSeqNbr(Company:string, AllocID:string, ParamNbr:string, SrcSeqNbr:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcNFSrcs(" + Company + "," + AllocID + "," + ParamNbr + "," + SrcSeqNbr + ")", {
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
   Description: Get AlcParamsBAQs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcParamsBAQs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcParamsBAQRow
   */  
export function get_AlcParamsBAQs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcParamsBAQRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParamsBAQs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcParamsBAQRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcParamsBAQs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcParamsBAQRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcParamsBAQRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlcParamsBAQs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParamsBAQs", {
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
   Summary: Calls GetByID to retrieve the AlcParamsBAQ item
   Description: Calls GetByID to retrieve the AlcParamsBAQ item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcParamsBAQ
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param BAQExportID Desc: BAQExportID   Required: True   Allow empty value : True
      @param BAQParamValNbr Desc: BAQParamValNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcParamsBAQRow
   */  
export function get_AlcParamsBAQs_Company_AllocID_ParamNbr_BAQExportID_BAQParamValNbr(Company:string, AllocID:string, ParamNbr:string, BAQExportID:string, BAQParamValNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcParamsBAQRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParamsBAQs(" + Company + "," + AllocID + "," + ParamNbr + "," + BAQExportID + "," + BAQParamValNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcParamsBAQRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlcParamsBAQ for the service
   Description: Calls UpdateExt to update AlcParamsBAQ. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcParamsBAQ
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param BAQExportID Desc: BAQExportID   Required: True   Allow empty value : True
      @param BAQParamValNbr Desc: BAQParamValNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcParamsBAQRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlcParamsBAQs_Company_AllocID_ParamNbr_BAQExportID_BAQParamValNbr(Company:string, AllocID:string, ParamNbr:string, BAQExportID:string, BAQParamValNbr:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParamsBAQs(" + Company + "," + AllocID + "," + ParamNbr + "," + BAQExportID + "," + BAQParamValNbr + ")", {
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
   Summary: Call UpdateExt to delete AlcParamsBAQ item
   Description: Call UpdateExt to delete AlcParamsBAQ item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcParamsBAQ
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param BAQExportID Desc: BAQExportID   Required: True   Allow empty value : True
      @param BAQParamValNbr Desc: BAQParamValNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlcParamsBAQs_Company_AllocID_ParamNbr_BAQExportID_BAQParamValNbr(Company:string, AllocID:string, ParamNbr:string, BAQExportID:string, BAQParamValNbr:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParamsBAQs(" + Company + "," + AllocID + "," + ParamNbr + "," + BAQExportID + "," + BAQParamValNbr + ")", {
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
   Description: Get AlcRanges items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcRanges
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcRangeRow
   */  
export function get_AlcRanges(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcRangeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcRanges", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcRangeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcRanges
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcRangeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcRangeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlcRanges(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcRanges", {
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
   Summary: Calls GetByID to retrieve the AlcRange item
   Description: Calls GetByID to retrieve the AlcRange item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcRange
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcRangeRow
   */  
export function get_AlcRanges_Company_AllocID_ParamNbr_SegmentNbr(Company:string, AllocID:string, ParamNbr:string, SegmentNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcRangeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcRanges(" + Company + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcRangeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlcRange for the service
   Description: Calls UpdateExt to update AlcRange. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcRange
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcRangeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlcRanges_Company_AllocID_ParamNbr_SegmentNbr(Company:string, AllocID:string, ParamNbr:string, SegmentNbr:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcRanges(" + Company + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")", {
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
   Summary: Call UpdateExt to delete AlcRange item
   Description: Call UpdateExt to delete AlcRange item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcRange
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlcRanges_Company_AllocID_ParamNbr_SegmentNbr(Company:string, AllocID:string, ParamNbr:string, SegmentNbr:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcRanges(" + Company + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")", {
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
   Description: Get AlcTargets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcTargets
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcTargetRow
   */  
export function get_AlcTargets(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcTargetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcTargets", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcTargetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcTargets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcTargetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcTargetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlcTargets(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcTargets", {
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
   Summary: Calls GetByID to retrieve the AlcTarget item
   Description: Calls GetByID to retrieve the AlcTarget item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcTarget
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param AllocTgtNbr Desc: AllocTgtNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcTargetRow
   */  
export function get_AlcTargets_Company_AllocID_AllocTgtNbr(Company:string, AllocID:string, AllocTgtNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcTargetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcTargets(" + Company + "," + AllocID + "," + AllocTgtNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcTargetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlcTarget for the service
   Description: Calls UpdateExt to update AlcTarget. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcTarget
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param AllocTgtNbr Desc: AllocTgtNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcTargetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlcTargets_Company_AllocID_AllocTgtNbr(Company:string, AllocID:string, AllocTgtNbr:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcTargets(" + Company + "," + AllocID + "," + AllocTgtNbr + ")", {
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
   Summary: Call UpdateExt to delete AlcTarget item
   Description: Call UpdateExt to delete AlcTarget item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcTarget
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param AllocTgtNbr Desc: AllocTgtNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlcTargets_Company_AllocID_AllocTgtNbr(Company:string, AllocID:string, AllocTgtNbr:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcTargets(" + Company + "," + AllocID + "," + AllocTgtNbr + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHedListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHedListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHedListRow)
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
export function get_GetRows(whereClauseAlcHed:string, whereClauseAlcAcct:string, whereClauseAlcAcctCat:string, whereClauseAlcJrnCd:string, whereClauseAlcParams:string, whereClauseAlcNFSrc:string, whereClauseAlcParamsBAQ:string, whereClauseAlcRange:string, whereClauseAlcTarget:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseAlcHed!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlcHed=" + whereClauseAlcHed
   }
   if(typeof whereClauseAlcAcct!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlcAcct=" + whereClauseAlcAcct
   }
   if(typeof whereClauseAlcAcctCat!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlcAcctCat=" + whereClauseAlcAcctCat
   }
   if(typeof whereClauseAlcJrnCd!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlcJrnCd=" + whereClauseAlcJrnCd
   }
   if(typeof whereClauseAlcParams!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlcParams=" + whereClauseAlcParams
   }
   if(typeof whereClauseAlcNFSrc!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlcNFSrc=" + whereClauseAlcNFSrc
   }
   if(typeof whereClauseAlcParamsBAQ!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlcParamsBAQ=" + whereClauseAlcParamsBAQ
   }
   if(typeof whereClauseAlcRange!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlcRange=" + whereClauseAlcRange
   }
   if(typeof whereClauseAlcTarget!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlcTarget=" + whereClauseAlcTarget
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/GetRows" + params, {
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
export function get_GetByID(allocID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof allocID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "allocID=" + allocID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/GetList" + params, {
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
   Summary: Invoke method getExternalMasterCOA
   Description: Purpose:  Get the Master COA from the proposted External Company
Parameters:  ProposedExtCompID
   OperationID: getExternalMasterCOA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getExternalMasterCOA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getExternalMasterCOA_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_getExternalMasterCOA(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/getExternalMasterCOA", {
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
   Summary: Invoke method ChangeExtCompanyID
   Description: This method resets the regular and Multi-Company G/L Accounts and the Reference Codes
when the External Company ID changes.
Parameters:
<param name="ProposedExtCompID">Proposed company ID</param><param name="allocID">AllocID from the AlcHed</param><param name="ds">The GL Journal Entry data set </param>
Notes:
   OperationID: ChangeExtCompanyID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeExtCompanyID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeExtCompanyID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeExtCompanyID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/ChangeExtCompanyID", {
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
   Summary: Invoke method createNewBAQParams
   Description: Purpose:called when BAQExportID is changed
Parameters:
<param name="ipBAQExportID">BAQ identifier</param><param name="ipAllocID">Allocation code</param><param name="ipParamNbr">Formula parameter number</param><param name="ds">GL Allocations Data Set</param>
Notes:
   OperationID: createNewBAQParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/createNewBAQParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/createNewBAQParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_createNewBAQParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/createNewBAQParams", {
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
   Summary: Invoke method ChangeAllocOption
   Description: Purpose:warn user if targets exist
Parameters:
<param name="ipProposedAllocOption">proposed allocation option</param><param name="ds">GL Allocations Data Set</param><param name="opWarningMessage">warning message</param>
Notes:
   OperationID: ChangeAllocOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAllocOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAllocOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeAllocOption(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/ChangeAllocOption", {
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
   Summary: Invoke method ChangeAllocationType
   Description: Purpose:warn user if targets exist
Parameters:
<param name="ipProposedAllocType">proposed allocation type</param><param name="ds">GL Allocations Data Set</param>
Notes:
   OperationID: ChangeAllocationType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAllocationType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAllocationType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeAllocationType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/ChangeAllocationType", {
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
   Summary: Invoke method ChangeBAQEntryType
   Description: Purpose:
Parameters:
<param name="ds">GL Allocations Data Set</param>
   OperationID: ChangeBAQEntryType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBAQEntryType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBAQEntryType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeBAQEntryType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/ChangeBAQEntryType", {
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
   Summary: Invoke method ChangeLookupEntryType
   Description: Purpose:
Parameters:
<param name="ipAllocID">Allocation code</param><param name="ipParamNbr">Parameter number</param><param name="ipSrcSeqNbr">Source srquence number</param><param name="ds">GL Allocations Data Set</param>
   OperationID: ChangeLookupEntryType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLookupEntryType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLookupEntryType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeLookupEntryType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/ChangeLookupEntryType", {
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
   Summary: Invoke method CheckArgument
   Description: Validate Argument1 and Argument2 values and return the values in the rigth format.
   OperationID: CheckArgument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckArgument_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckArgument_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckArgument(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/CheckArgument", {
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
   Summary: Invoke method CheckBAQExportID
   Description: Validate BAQ Export ID
   OperationID: CheckBAQExportID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBAQExportID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBAQExportID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckBAQExportID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/CheckBAQExportID", {
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
   Summary: Invoke method CheckBAQParameter
   Description: Purpose:  Validate the parameter field is a valid BAQ parameter
Parameters:
<param name="ipBAQExportID">ipBAQExportID">BAQ to validate the parameter</param><param name="ipFieldName">Field to validate</param>
Notes:
   OperationID: CheckBAQParameter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBAQParameter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBAQParameter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckBAQParameter(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/CheckBAQParameter", {
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
   Summary: Invoke method CheckBAQParameterValue
   Description: Purpose:  validate the value entered for the query field to ensure it is a valid type
Parameters:
<param name="ipBAQExportID">ipBAQExportID">BAQ to validate the parameter</param><param name="ipFieldName">Field to validate</param><param name="ipValue">query field value to validate</param>
Notes:
   OperationID: CheckBAQParameterValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBAQParameterValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBAQParameterValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckBAQParameterValue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/CheckBAQParameterValue", {
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
   Summary: Invoke method CheckBook
   Description: Validate the selected book is valid and of type standard
   OperationID: CheckBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckBook(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/CheckBook", {
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
   Summary: Invoke method CheckCanAddNewTarget
   Description: Purpose: If fixedvalue and current sum of percent equals total then do not allow add
Parameters:
<param name="ipAllocID">Allocation Code</param>
Notes:
   OperationID: CheckCanAddNewTarget
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCanAddNewTarget_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCanAddNewTarget_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCanAddNewTarget(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/CheckCanAddNewTarget", {
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
   Summary: Invoke method CheckCategory
   Description: Validate Category
   OperationID: CheckCategory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCategory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCategory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCategory(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/CheckCategory", {
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
   Summary: Invoke method CheckForDuplicateAccount
   Description: Purpose:  Ensure an account is only entered once as a source
Parameters:
<param name="ipGLAccount">proposed GL Account</param><param name="ipParamNbr">parameter nbr</param><param name="ipAllocID">allocation id</param>
   OperationID: CheckForDuplicateAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckForDuplicateAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForDuplicateAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckForDuplicateAccount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/CheckForDuplicateAccount", {
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
   Summary: Invoke method CheckJournalCode
   Description: Validate Journal Code
   OperationID: CheckJournalCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckJournalCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckJournalCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckJournalCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/CheckJournalCode", {
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
   Summary: Invoke method CheckMinMax
   Description: Validate Min and max values
   OperationID: CheckMinMax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckMinMax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckMinMax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckMinMax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/CheckMinMax", {
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
   Summary: Invoke method CheckParamName
   Description: Validate parameter name is not a valid math operator.
   OperationID: CheckParamName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckParamName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckParamName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckParamName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/CheckParamName", {
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
   Summary: Invoke method CheckParamOption
   Description: Purpose:
Parameters:  none
<param name="ipAllocID">Allocation code</param><param name="ipParamNbr">parameter number</param><param name="ipSrcSeqNbr">Source sequence number</param><param name="ipParamOpt">parameter option</param><param name="ds">GL Allocations Data Set</param>
   OperationID: CheckParamOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckParamOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckParamOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckParamOption(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/CheckParamOption", {
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
   Summary: Invoke method CheckParamOptionBAQ
   Description: Purpose:
Parameters:  none
<param name="ipParamOpt">parameter option</param><param name="ds">GL Allocations Data Set</param>
   OperationID: CheckParamOptionBAQ
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckParamOptionBAQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckParamOptionBAQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckParamOptionBAQ(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/CheckParamOptionBAQ", {
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
   Summary: Invoke method CheckParamSegment
   Description: Purpose:
Parameters:  none
<param name="ipParamSegmentNbr">parameter option</param><param name="ipParamType">either NonFin or BAQ</param><param name="ds">GL Allocations Data Set</param>
   OperationID: CheckParamSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckParamSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckParamSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckParamSegment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/CheckParamSegment", {
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
   Summary: Invoke method CheckPercentageToAllocate
   Description: Purpose: Warn the user if the percentage to allocate on the allocation code > 100.
Parameters:
<param name="ipAllocID">Allocation Code</param><param name="ipProposedPercentage">percent to allocate</param><param name="opWarnMsg">warning message</param>
Notes:
   OperationID: CheckPercentageToAllocate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPercentageToAllocate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPercentageToAllocate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPercentageToAllocate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/CheckPercentageToAllocate", {
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
   Summary: Invoke method CheckPriorTgtStamp
   Description: Purpose:
Parameters:
<param name="ipPriorTgtStamp">proposed source allocation stamp</param><param name="ds">GL Allocations Data Set</param><param name="opWarningMsg">warning message</param>
Notes:
   OperationID: CheckPriorTgtStamp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPriorTgtStamp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPriorTgtStamp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPriorTgtStamp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/CheckPriorTgtStamp", {
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
   Summary: Invoke method CheckSegmentNbr
   Description: This method is to be used in place of GetNewAlcRange.  This method Validates
there are still COA Segments available.
   OperationID: CheckSegmentNbr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSegmentNbr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSegmentNbr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckSegmentNbr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/CheckSegmentNbr", {
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
   Summary: Invoke method CheckSyntax
   Description: Check Syntax for formula field.
   OperationID: CheckSyntax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSyntax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSyntax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckSyntax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/CheckSyntax", {
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
   Summary: Invoke method CheckTgtStamp
   Description: Purpose:
Parameters:
<param name="ipTgtStamp">outgoing allocation mark</param><param name="ds">GL Allocations Data Set</param><param name="opWarningMsg">warning message</param>
Notes:
   OperationID: CheckTgtStamp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTgtStamp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTgtStamp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckTgtStamp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/CheckTgtStamp", {
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
   Summary: Invoke method CheckTier
   Description: Purpose:
Parameters:
<param name="ipTier">proposed tier</param><param name="ds">GL Allocations Data Set</param>
Notes:
   OperationID: CheckTier
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTier_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTier_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckTier(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/CheckTier", {
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
   Summary: Invoke method CheckTotalPercent
   Description: Purpose:
Parameters:
<param name="ipProposedPercent">Proposed percent</param><param name="ds">GL Allocations Data Set</param><param name="opTotalPercent">Total percent</param>
Notes:
   OperationID: CheckTotalPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTotalPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTotalPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckTotalPercent(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/CheckTotalPercent", {
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
   Summary: Invoke method CreateAlcNFSrcRecords
   Description: Create Source Fields Records for the selected MapUID
   OperationID: CreateAlcNFSrcRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateAlcNFSrcRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateAlcNFSrcRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateAlcNFSrcRecords(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/CreateAlcNFSrcRecords", {
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
   Summary: Invoke method GetLinkList
   Description: Returns a List of valid values for the cmbLinkUID Combo-box
   OperationID: GetLinkList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLinkList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLinkList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLinkList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/GetLinkList", {
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
   Summary: Invoke method GetLookupSrcCodeID
   Description: Returns the Source Field Code in Invariant Format
   OperationID: GetLookupSrcCodeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLookupSrcCodeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLookupSrcCodeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLookupSrcCodeID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/GetLookupSrcCodeID", {
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
   Summary: Invoke method GetNewAlcNFSrc1
   Description: This method is to be used in place of GetNewAlcNFSrc.  This method Validates
that only one AlcNFSrc record is created for each AlcParam record created.
   OperationID: GetNewAlcNFSrc1
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcNFSrc1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcNFSrc1_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcNFSrc1(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/GetNewAlcNFSrc1", {
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
   Summary: Invoke method GetNewAlcRange1
   Description: This method is to be used in place of GetNewAlcRange.  This method Validates
there are still COA Segments available.
   OperationID: GetNewAlcRange1
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcRange1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcRange1_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcRange1(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/GetNewAlcRange1", {
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
   Summary: Invoke method GetOperatorsList
   Description: Return a list of valid operators in a format ready to be use on a combo-box
   OperationID: GetOperatorsList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOperatorsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOperatorsList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/GetOperatorsList", {
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
   Summary: Invoke method GetOperatorsMenuList
   Description: Return a list of valid operators in a format ready to be use on the context Menu
(i.e - +'Operators~-'Operators~*'Operators~/'Operators~('Operators~)'Operators
   OperationID: GetOperatorsMenuList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOperatorsMenuList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOperatorsMenuList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/GetOperatorsMenuList", {
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
   Summary: Invoke method GetParametersList
   Description: Return a list of available parameters in a format ready to be use on a combo-box
   OperationID: GetParametersList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetParametersList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetParametersList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetParametersList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/GetParametersList", {
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
   Summary: Invoke method GetParamMenuList
   Description: Return a list of available parameters in a format ready to be use on the context Menu
   OperationID: GetParamMenuList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetParamMenuList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetParamMenuList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetParamMenuList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/GetParamMenuList", {
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
   Summary: Invoke method RefreshAllocationTotals
   Description: Purpose:
Parameters:
<param name="ds">GL Allocations Data Set</param>
Notes:
   OperationID: RefreshAllocationTotals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshAllocationTotals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshAllocationTotals_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshAllocationTotals(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/RefreshAllocationTotals", {
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
   Summary: Invoke method RetrieveGLAcctDesc
   Description: Purpose:
<param name="ipType">source or target</param><param name="ds">GL Allocations Data Set</param>
Notes: Do not use, method is obsolete since 11.2.100. DisplayGLAccountDesc field is obsolete in object. Please use GLAcctDispAccountDesc field.
   OperationID: RetrieveGLAcctDesc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RetrieveGLAcctDesc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrieveGLAcctDesc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RetrieveGLAcctDesc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/RetrieveGLAcctDesc", {
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
   Summary: Invoke method UpdateAcctBalAcct
   Description: Updates Account Balance Account.
   OperationID: UpdateAcctBalAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateAcctBalAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAcctBalAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateAcctBalAcct(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/UpdateAcctBalAcct", {
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
   Summary: Invoke method ValidatePercentTotals
   Description: Purpose:  warn the user if the sum of the AlcTarget.RatioValue != AlcHed.PercentToAllocate
Parameters:
<param name="ipAllocID">allocation id</param><param name="opWarnMsg">warning message</param>
Notes:
   OperationID: ValidatePercentTotals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePercentTotals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePercentTotals_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePercentTotals(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/ValidatePercentTotals", {
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
   Summary: Invoke method ValidTgtNatSegment
   Description: Purpose:  warn the user if Natural Segment Statistical option not set to Both
Parameters:
<param name="ipSegment">COA Segment Value to validate</param><param name="ipAllocID">Allocation Code</param><param name="opWarnMsg">warning message</param>
Notes:
   OperationID: ValidTgtNatSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidTgtNatSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidTgtNatSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidTgtNatSegment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/ValidTgtNatSegment", {
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
   Summary: Invoke method ValidParamNatSegment
   Description: Purpose:  warn the user if Natural Segment Statistical option is set to No
Parameters:
<param name="ipSegment">COA Segment Value to validate</param><param name="ipAllocID">Allocation Code</param><param name="ipParamNbr">Parameter number</param><param name="opWarnMsg">warning message</param>
Notes:
   OperationID: ValidParamNatSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidParamNatSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidParamNatSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidParamNatSegment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/ValidParamNatSegment", {
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
   Summary: Invoke method MaskValidate
   Description: Test if account masks are valid
   OperationID: MaskValidate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MaskValidate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MaskValidate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MaskValidate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/MaskValidate", {
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
   Summary: Invoke method GetNewAlcHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcHed(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/GetNewAlcHed", {
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
   Summary: Invoke method GetNewAlcAcct
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcAcct(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/GetNewAlcAcct", {
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
   Summary: Invoke method GetNewAlcAcctCat
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcAcctCat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcAcctCat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcAcctCat_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcAcctCat(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/GetNewAlcAcctCat", {
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
   Summary: Invoke method GetNewAlcJrnCd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcJrnCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcJrnCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcJrnCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcJrnCd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/GetNewAlcJrnCd", {
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
   Summary: Invoke method GetNewAlcParams
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/GetNewAlcParams", {
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
   Summary: Invoke method GetNewAlcNFSrc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcNFSrc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcNFSrc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcNFSrc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcNFSrc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/GetNewAlcNFSrc", {
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
   Summary: Invoke method GetNewAlcParamsBAQ
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcParamsBAQ
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcParamsBAQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcParamsBAQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcParamsBAQ(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/GetNewAlcParamsBAQ", {
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
   Summary: Invoke method GetNewAlcRange
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcRange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/GetNewAlcRange", {
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
   Summary: Invoke method GetNewAlcTarget
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcTarget
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcTarget_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcTarget_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcTarget(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/GetNewAlcTarget", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcAcctCatRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcAcctCatRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcAcctRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcAcctRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHedListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcHedListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcHedRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcJrnCdRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcJrnCdRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcNFSrcRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcNFSrcRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcParamsBAQRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcParamsBAQRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcParamsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcParamsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcRangeRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcRangeRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcTargetRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcTargetRow[],
}

export interface Erp_Tablesets_AlcAcctCatRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**   Intended for internal use only to keep the records unique.  The ParamNbr value is 0  when tied to a source account (AlcHed).
When tied to a parameter criteria (AlcParams) it inherits its value from AlcParams table.  */  
   "ParamNbr":number,
      /**  Unique identifier of this category of accounts.  */  
   "CategoryID":string,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "AlcAcctCatCOAActCatType":string,
   "AlcAcctCatCOAActCatDescription":string,
   "COADescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AlcAcctRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**   Intended for internal use only to keep the records unique.  The ParamNbr value is 0  when tied to a source account (AlcHed).
When tied to a parameter criteria (AlcParams) it inherits its value from AlcParams table.  */  
   "ParamNbr":number,
      /**  GL Account or GL Account mask  */  
   "AllocGLAcct":string,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Allocation Segment Value 1  */  
   "AllocSegValue1":string,
      /**  Allocation Segment Value 2  */  
   "AllocSegValue2":string,
      /**  Allocation Segment Value 3  */  
   "AllocSegValue3":string,
      /**  Allocation Segment Value 4  */  
   "AllocSegValue4":string,
      /**  Allocation Segment Value 5  */  
   "AllocSegValue5":string,
      /**  Allocation Segment Value 6  */  
   "AllocSegValue6":string,
      /**  Allocation Segment Value 7  */  
   "AllocSegValue7":string,
      /**  Allocation Segment Value 8  */  
   "AllocSegValue8":string,
      /**  Allocation Segment Value 9  */  
   "AllocSegValue9":string,
      /**  Allocation Segment Value 10  */  
   "AllocSegValue10":string,
      /**  Allocation Segment Value 11  */  
   "AllocSegValue11":string,
      /**  Allocation Segment Value 12  */  
   "AllocSegValue12":string,
      /**  Allocation Segment Value 13  */  
   "AllocSegValue13":string,
      /**  Allocation Segment Value 14  */  
   "AllocSegValue14":string,
      /**  Allocation Segment Value 15  */  
   "AllocSegValue15":string,
      /**  Allocation Segment Value 16  */  
   "AllocSegValue16":string,
      /**  Allocation Segment Value 17  */  
   "AllocSegValue17":string,
      /**  Allocation Segment Value 18  */  
   "AllocSegValue18":string,
      /**  Allocation Segment Value 19  */  
   "AllocSegValue19":string,
      /**  Allocation Segment Value 20  */  
   "AllocSegValue20":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "COADescription":string,
   "GLAcctDispGLAcctDisp":string,
   "GLAcctDispGLShortAcct":string,
   "GLAcctDispAccountDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AlcHedListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  Allocation code description.  */  
   "Description":string,
      /**   Identifies whether or not the allocaiton is balance or transaction based.  1 = Transaction and is the default value.
2 = Balance based.  */  
   "AllocationType":number,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Allocation tier.  */  
   "Tier":number,
      /**  Identifies the allocation stamp to which this allocation is to be applied.  */  
   "PriorTgtStamp":string,
      /**  Identifies the allocation stamp that is to to be stamped on the GLJrnDtls.  */  
   "TgtStamp":string,
      /**  Identifies the allocation stamp that was processed by this allocation.  */  
   "SrcAllocStamp":string,
      /**  When Yes the Allocation Engine ignores the allocation stamp assigned to the GLJrnDtl when determining if a entry is subject to allocations for the current allocation code.  */  
   "IgnoreStamp":boolean,
      /**  Yes indicates that all allocation stamps are valid for the allocation code.  */  
   "UseAllStamps":boolean,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  */  
   "AllocOption":number,
      /**  Postive, fractional value indicating how much of a source is allocated.  Default value is 100.00.  */  
   "PercentToAlloc":number,
      /**  Indicates if the allocation units are used.  */  
   "UseAllocUnits":boolean,
      /**  The general ledger account the allocation is to be written off.  */  
   "OffsetAcct":string,
      /**  Offset Segment Value 1  */  
   "OffsetSegVal1":string,
      /**  Offset Segment Value 2  */  
   "OffsetSegVal2":string,
      /**  Offset Segment Value 3  */  
   "OffsetSegVal3":string,
      /**  Offset Segment Value 4  */  
   "OffsetSegVal4":string,
      /**  Offset Segment Value 5  */  
   "OffsetSegVal5":string,
      /**  Offset Segment Value 6  */  
   "OffsetSegVal6":string,
      /**  Offset Segment Value 7  */  
   "OffsetSegVal7":string,
      /**  Offset Segment Value 8  */  
   "OffsetSegVal8":string,
      /**  Offset Segment Value 9  */  
   "OffsetSegVal9":string,
      /**  Offset Segment Value 10  */  
   "OffsetSegVal10":string,
      /**  Offset Segment Value 11  */  
   "OffsetSegVal11":string,
      /**  Offset Segment Value 12  */  
   "OffsetSegVal12":string,
      /**  Offset Segment Value 13  */  
   "OffsetSegVal13":string,
      /**  Offset Segment Value 14  */  
   "OffsetSegVal14":string,
      /**  Offset Segment Value 15  */  
   "OffsetSegVal15":string,
      /**  Offset Segment Value 16  */  
   "OffsetSegVal16":string,
      /**  Offset Segment Value 17  */  
   "OffsetSegVal17":string,
      /**  Offset Segment Value 18  */  
   "OffsetSegVal18":string,
      /**  Offset Segment Value 19  */  
   "OffsetSegVal19":string,
      /**  Offset Segment Value 20  */  
   "OffsetSegVal20":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates whether or not a allocation is currently executing.  */  
   "AllocIsRunning":boolean,
      /**  Total allocation units.  This is the sum of the allocation units defined on the targets.  */  
   "TotalAllocUnits":number,
      /**  his is the sum of the percentage values defined on the targets.  */  
   "TotalPercentage":number,
   "OffsetAcctDesc":string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   "GLAcctDispGLAcctDisp":string,
      /**  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The value of this field is the concatenation of the first three controlled display order segments.  For example, if a chart has 5 controlled segments that are displayed in the following order: seg5->seg3->seg4->seg2->seg1, this field contains the concatention of seg5->seg3->seg4 up to th  */  
   "GLAcctDispGLShortAcct":string,
      /**  Text that describes the account.  */  
   "GLAcctDispAccountDesc":string,
      /**  Descripiton of Book  */  
   "GLBookDescription":string,
      /**  Indicates the base currency for the book  */  
   "GLBookCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AlcHedRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  Allocation code description.  */  
   "Description":string,
      /**   Identifies whether or not the allocaiton is balance or transaction based.  1 = Transaction and is the default value.
2 = Balance based.  */  
   "AllocationType":number,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Allocation tier.  */  
   "Tier":number,
      /**  Identifies the allocation stamp to which this allocation is to be applied.  */  
   "PriorTgtStamp":string,
      /**  Identifies the allocation stamp that is to to be stamped on the GLJrnDtls.  */  
   "TgtStamp":string,
      /**  Identifies the allocation stamp that was processed by this allocation.  */  
   "SrcAllocStamp":string,
      /**  When Yes the Allocation Engine ignores the allocation stamp assigned to the GLJrnDtl when determining if a entry is subject to allocations for the current allocation code.  */  
   "IgnoreStamp":boolean,
      /**  Yes indicates that all allocation stamps are valid for the allocation code.  */  
   "UseAllStamps":boolean,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  */  
   "AllocOption":number,
      /**  Postive, fractional value indicating how much of a source is allocated.  Default value is 100.00.  */  
   "PercentToAlloc":number,
      /**  Indicates if the allocation units are used.  */  
   "UseAllocUnits":boolean,
      /**  The general ledger account the allocation is to be written off.  */  
   "OffsetAcct":string,
      /**  Offset Segment Value 1  */  
   "OffsetSegVal1":string,
      /**  Offset Segment Value 2  */  
   "OffsetSegVal2":string,
      /**  Offset Segment Value 3  */  
   "OffsetSegVal3":string,
      /**  Offset Segment Value 4  */  
   "OffsetSegVal4":string,
      /**  Offset Segment Value 5  */  
   "OffsetSegVal5":string,
      /**  Offset Segment Value 6  */  
   "OffsetSegVal6":string,
      /**  Offset Segment Value 7  */  
   "OffsetSegVal7":string,
      /**  Offset Segment Value 8  */  
   "OffsetSegVal8":string,
      /**  Offset Segment Value 9  */  
   "OffsetSegVal9":string,
      /**  Offset Segment Value 10  */  
   "OffsetSegVal10":string,
      /**  Offset Segment Value 11  */  
   "OffsetSegVal11":string,
      /**  Offset Segment Value 12  */  
   "OffsetSegVal12":string,
      /**  Offset Segment Value 13  */  
   "OffsetSegVal13":string,
      /**  Offset Segment Value 14  */  
   "OffsetSegVal14":string,
      /**  Offset Segment Value 15  */  
   "OffsetSegVal15":string,
      /**  Offset Segment Value 16  */  
   "OffsetSegVal16":string,
      /**  Offset Segment Value 17  */  
   "OffsetSegVal17":string,
      /**  Offset Segment Value 18  */  
   "OffsetSegVal18":string,
      /**  Offset Segment Value 19  */  
   "OffsetSegVal19":string,
      /**  Offset Segment Value 20  */  
   "OffsetSegVal20":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates if Statistical Balance of Target Account should be used as Allocation Units  */  
   "StatBalAsAllocUnits":boolean,
      /**  Indicates whether or not a allocation is currently executing.  */  
   "AllocIsRunning":boolean,
      /**  Total allocation units.  This is the sum of the allocation units defined on the targets.  */  
   "TotalAllocUnits":number,
      /**  his is the sum of the percentage values defined on the targets.  */  
   "TotalPercentage":number,
   "OffsetAcctDesc":string,
   "BitFlag":number,
   "GLAcctDispGLAcctDisp":string,
   "GLAcctDispAccountDesc":string,
   "GLAcctDispGLShortAcct":string,
   "GLBookDescription":string,
   "GLBookCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AlcJrnCdRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**   Intended for internal use only to keep the records unique.  The ParamNbr value is 0  when tied to a source account (AlcHed).
When tied to a parameter criteria (AlcParams) it inherits its value from AlcParams table.  */  
   "ParamNbr":number,
      /**  Unique identifier of the journal used to group entries. The user can create their own journal codes to be used instead of the default codes.  */  
   "JournalCode":string,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "JrnlCodeJrnlDescription":string,
   "JrnlCodeSystemJournal":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AlcNFSrcRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  Intended for internal use only to keep the records unique.  The value is inherited from the AlcParams table.  */  
   "ParamNbr":number,
      /**  LookupTblMapUID_obsolete  */  
   "LookupTblMapUID_obsolete":number,
      /**  TgtSeqNbr_obsolete  */  
   "TgtSeqNbr_obsolete":number,
      /**  LinkUID_obsolete  */  
   "LinkUID_obsolete":number,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**   Identifes the option for the BAQ parameter.
1 = Use Target Account Segment.  
2 = Use Source Account Segment
3 = Use Allocation Run Start Date
4 = Use allocation Run End Date  */  
   "ParamOpt":number,
      /**  Identifies the segment number to use to determine the segment code that will be used to look up the result value in the lookup table.  */  
   "ParamSegmentNbr":number,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Identifies if the parameter is an actual value or an option.  */  
   "EntryType":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  SrcSeqNbr  */  
   "SrcSeqNbr":number,
      /**  SrcCodeID  */  
   "SrcCodeID":string,
      /**  List of LookupLink records for the cmbLinkUID combo  */  
   "LinkList":string,
      /**  Source Field Link Description (Summ of Lookup Link Field1 to Field30 and Value1 to Value30 information)  */  
   "SrcFieldDesc":string,
   "SrcFieldName":string,
   "DspSrcCodeID":string,
   "SrcDataType":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AlcParamsBAQRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  Intended for internal use only to keep the records unique.  */  
   "ParamNbr":number,
      /**  Intended for internal use only to keep the records unique.  */  
   "BAQParamValNbr":number,
      /**  BAQ ID, the unique identifier for this Query table within the company  */  
   "BAQExportID":string,
   "ParameterName":string,
      /**  Specific baq parameter value.  */  
   "BAQParamCode":string,
      /**   Identifes the option for the BAQ parameter.
1 = Use Target Account Segment.  
2 = Use Source Account Segment
3 = Use Allocation Run Start Date
4 = Use allocation Run End Date  */  
   "ParamOpt":number,
      /**  Identifies the segment number to use to determine the segment code that will be used to look up the result value in the lookup table.  */  
   "ParamSegmentNbr":number,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Identifies if the parameter is an actual value or an option.  */  
   "EntryType":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "ParamSegmentName":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AlcParamsRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  Intended for internal use only to keep the records unique.  */  
   "ParamNbr":number,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  The name assigned to a parameter.  This name must be unique.  */  
   "ParamName":string,
      /**  Identifies the type of parameter used in the allocation logic.  1 = Account Balances, 2 = Summarized balances,  3 = BAQ and 4 = Non Financial Data.  */  
   "ParamType":number,
      /**  Text that describes the parameter.  */  
   "ParamDesc":string,
      /**  Indicates the source data for the value of a parameter value when the parameter is of type Account Balance.  */  
   "AcctParamValSrc":number,
      /**  Indicates the source data for the value of a parameter value when the parameter is of type Summarized.  */  
   "SumParamValSrc":number,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Account balance account.  Only valid when the formula type = 1.  */  
   "AcctBalAcct":string,
      /**  Account Segment Value 1  */  
   "AcctBalSegVal1":string,
      /**  Account Segment Value 2  */  
   "AcctBalSegVal2":string,
      /**  Account Segment Value 3  */  
   "AcctBalSegVal3":string,
      /**  Account Segment Value 4  */  
   "AcctBalSegVal4":string,
      /**  Account Segment Value 5  */  
   "AcctBalSegVal5":string,
      /**  Account Segment Value 6  */  
   "AcctBalSegVal6":string,
      /**  Account Segment Value 7  */  
   "AcctBalSegVal7":string,
      /**  Account Segment Value 8  */  
   "AcctBalSegVal8":string,
      /**  Account Segment Value 9  */  
   "AcctBalSegVal9":string,
      /**  Account Segment Value 10  */  
   "AcctBalSegVal10":string,
      /**  Account Segment Value 11  */  
   "AcctBalSegVal11":string,
      /**  Account Segment Value 12  */  
   "AcctBalSegVal12":string,
      /**  Account Segment Value 13  */  
   "AcctBalSegVal13":string,
      /**  Account Segment Value 14  */  
   "AcctBalSegVal14":string,
      /**  Account Segment Value 15  */  
   "AcctBalSegVal15":string,
      /**  Account Segment Value 16  */  
   "AcctBalSegVal16":string,
      /**  Account Segment Value 17  */  
   "AcctBalSegVal17":string,
      /**  Account Segment Value 18  */  
   "AcctBalSegVal18":string,
      /**  Account Segment Value 19  */  
   "AcctBalSegVal19":string,
      /**  Account Segment Value 20  */  
   "AcctBalSegVal20":string,
      /**  Yes indictes the target account's balance is taken and the AcctBalAcct is set equal to the AlcTarget.TgtGLAcct.  This only only valid when the formula type = Account Balances.  */  
   "UseTgtAcct":boolean,
      /**  BAQ ID, the unique identifier for this Query table within the company  */  
   "BAQExportID":string,
      /**  Statistical UOM code.  */  
   "StatUOMCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  NFSrcMapUID  */  
   "NFSrcMapUID":number,
      /**  NFTgtSeqNbr  */  
   "NFTgtSeqNbr":number,
      /**  YTDBalance  */  
   "YTDBalance":boolean,
      /**  Indicates whether or not the BAQ has parameters defined.  If not, then the user cannot define BAQ parameters in allocation code maintenance.  */  
   "BAQEnableParams":boolean,
      /**  Dynamic query description  */  
   "BAQExportIDDescription":string,
   "BitFlag":number,
   "GLAcctDispGLShortAcct":string,
   "GLAcctDispAccountDesc":string,
   "GLAcctDispGLAcctDisp":string,
   "GLBookDescription":string,
   "GLBookCurrencyCode":string,
   "LookupTableIDDisplayName":string,
   "TargetFieldNameFieldName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AlcRangeRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**   Intended for internal use only to keep the records unique.  The ParamNbr value is 0  when tied to a source account (AlcHed).
When tied to a parameter criteria (AlcParams) it inherits its value from AlcParams table.  */  
   "ParamNbr":number,
      /**  System generated number from 1 through 20.  */  
   "SegmentNbr":number,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Minimum vale for range selection.  */  
   "MinValue":string,
      /**  Maximum value for range selection.  */  
   "MaxValue":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "COASegmentSegmentName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AlcTargetRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   "AllocTgtNbr":number,
      /**  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  */  
   "AllocOption":number,
      /**  Formula entered by the user used to calculate the allocation amount.  Only valid if the allocation option = 2.  */  
   "RatioFormula":string,
      /**  Postive, fractional value indicating how much of an allocation is applied to this target.  */  
   "RatioValue":number,
      /**   The relative  number of units used to allocate to this account.
Allocation units / Total Allocation units is used to distribute the amount. Total Allocation units are calculated for a given AllocID and not stored.  */  
   "AllocUnits":number,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  The GL Account an amount is allocated to.  This may be an actual GL Account or a masked account where each mask character is swapped with the corresponding character from the source GL Account.  */  
   "TgtGLAcct":string,
      /**  Target Segment Value 1  */  
   "TgtSegVal1":string,
      /**  Target Segment Value 2  */  
   "TgtSegVal2":string,
      /**  Target Segment Value 3  */  
   "TgtSegVal3":string,
      /**  Target Segment Value 4  */  
   "TgtSegVal4":string,
      /**  Target Segment Value 5  */  
   "TgtSegVal5":string,
      /**  Target Segment Value 6  */  
   "TgtSegVal6":string,
      /**  Target Segment Value 7  */  
   "TgtSegVal7":string,
      /**  Target Segment Value 8  */  
   "TgtSegVal8":string,
      /**  Target Segment Value 9  */  
   "TgtSegVal9":string,
      /**  Target Segment Value 10  */  
   "TgtSegVal10":string,
      /**  Target Segment Value 11  */  
   "TgtSegVal11":string,
      /**  Target Segment Value 12  */  
   "TgtSegVal12":string,
      /**  Target Segment Value 13  */  
   "TgtSegVal13":string,
      /**  Target Segment Value 14  */  
   "TgtSegVal14":string,
      /**  Target Segment Value 15  */  
   "TgtSegVal15":string,
      /**  Target Segment Value 16  */  
   "TgtSegVal16":string,
      /**  Target Segment Value 17  */  
   "TgtSegVal17":string,
      /**  Target Segment Value 18  */  
   "TgtSegVal18":string,
      /**  Target Segment Value 19  */  
   "TgtSegVal19":string,
      /**  Target Segment Value 20  */  
   "TgtSegVal20":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MultiCompany  */  
   "MultiCompany":boolean,
      /**  ExtCompanyID  */  
   "ExtCompanyID":string,
      /**  ExtGLAccount  */  
   "ExtGLAccount":string,
      /**  ExtCOACode  */  
   "ExtCOACode":string,
      /**  ExtSegValue1  */  
   "ExtSegValue1":string,
      /**  ExtSegValue2  */  
   "ExtSegValue2":string,
      /**  ExtSegValue3  */  
   "ExtSegValue3":string,
      /**  ExtSegValue4  */  
   "ExtSegValue4":string,
      /**  ExtSegValue5  */  
   "ExtSegValue5":string,
      /**  ExtSegValue6  */  
   "ExtSegValue6":string,
      /**  ExtSegValue7  */  
   "ExtSegValue7":string,
      /**  ExtSegValue8  */  
   "ExtSegValue8":string,
      /**  ExtSegValue9  */  
   "ExtSegValue9":string,
      /**  ExtSegValue10  */  
   "ExtSegValue10":string,
      /**  ExtSegValue11  */  
   "ExtSegValue11":string,
      /**  ExtSegValue12  */  
   "ExtSegValue12":string,
      /**  ExtSegValue13  */  
   "ExtSegValue13":string,
      /**  ExtSegValue14  */  
   "ExtSegValue14":string,
      /**  ExtSegValue15  */  
   "ExtSegValue15":string,
      /**  ExtSegValue16  */  
   "ExtSegValue16":string,
      /**  ExtSegValue17  */  
   "ExtSegValue17":string,
      /**  ExtSegValue18  */  
   "ExtSegValue18":string,
      /**  ExtSegValue19  */  
   "ExtSegValue19":string,
      /**  ExtSegValue20  */  
   "ExtSegValue20":string,
      /**  OverrideGLAcct  */  
   "OverrideGLAcct":boolean,
      /**  Used to bind UI control.  */  
   "Argument1":string,
      /**  Used to bind UI control.  */  
   "Argument2":string,
      /**  Used to bind UI control.  */  
   "Operator":string,
      /**  Target GL Account Description  */  
   "TgtGLDesc":string,
      /**  Ext GL Account Description  */  
   "ExtAccountDesc":string,
      /**  Flag to indicate if the MultiCompany check box needs to be enabled.  */  
   "EnableMultiCompany":boolean,
   "BitFlag":number,
   "GLAcctDispAccountDesc":string,
   "GLAcctDispGLShortAcct":string,
   "GLAcctDispGLAcctDisp":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ipProposedAllocOption
      @param ds
   */  
export interface ChangeAllocOption_input{
   ipProposedAllocOption:number,
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface ChangeAllocOption_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
   opWarningMessage:string,
}
}

   /** Required : 
      @param ipProposedAllocType
      @param ds
   */  
export interface ChangeAllocationType_input{
   ipProposedAllocType:number,
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface ChangeAllocationType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeBAQEntryType_input{
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface ChangeBAQEntryType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ProposedExtCompID
      @param allocID
      @param ds
   */  
export interface ChangeExtCompanyID_input{
   ProposedExtCompID:string,
   allocID:string,
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface ChangeExtCompanyID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ipAllocID
      @param ipParamNbr
      @param ipSrcSeqNbr
      @param ds
   */  
export interface ChangeLookupEntryType_input{
   ipAllocID:string,
   ipParamNbr:number,
   ipSrcSeqNbr:number,
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface ChangeLookupEntryType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ipAllocID
      @param ipArgument1
      @param ipArgument2
   */  
export interface CheckArgument_input{
      /**  ipAllocID of selected record  */  
   ipAllocID:string,
      /**  Argument1 to validate  */  
   ipArgument1:string,
      /**  Argument2 to validate  */  
   ipArgument2:string,
}

export interface CheckArgument_output{
parameters : {
      /**  output parameters  */  
   opArgument1:string,
   opArgument2:string,
}
}

   /** Required : 
      @param ipBAQExportID
      @param ds
   */  
export interface CheckBAQExportID_input{
      /**  BAQ proposed value  */  
   ipBAQExportID:string,
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface CheckBAQExportID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ipBAQExportID
      @param ipFieldName
      @param ipValue
   */  
export interface CheckBAQParameterValue_input{
   ipBAQExportID:string,
   ipFieldName:string,
   ipValue:string,
}

export interface CheckBAQParameterValue_output{
}

   /** Required : 
      @param ipBAQExportID
      @param ipFieldName
   */  
export interface CheckBAQParameter_input{
   ipBAQExportID:string,
   ipFieldName:string,
}

export interface CheckBAQParameter_output{
}

   /** Required : 
      @param ipBookID
      @param ds
   */  
export interface CheckBook_input{
      /**  GL Book ID  */  
   ipBookID:string,
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface CheckBook_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ipAllocID
   */  
export interface CheckCanAddNewTarget_input{
   ipAllocID:string,
}

export interface CheckCanAddNewTarget_output{
}

   /** Required : 
      @param ipCategoryID
      @param ds
   */  
export interface CheckCategory_input{
      /**  Category ID to validate  */  
   ipCategoryID:string,
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface CheckCategory_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ipGLAccount
      @param ipParamNbr
      @param ipAllocID
   */  
export interface CheckForDuplicateAccount_input{
   ipGLAccount:string,
   ipParamNbr:number,
   ipAllocID:string,
}

export interface CheckForDuplicateAccount_output{
}

   /** Required : 
      @param ipJournalCode
      @param ds
   */  
export interface CheckJournalCode_input{
      /**  Journal Code to validate  */  
   ipJournalCode:string,
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface CheckJournalCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ipMinRange
      @param ipMaxRange
      @param ipCOACode
      @param ipSegmentNbr
   */  
export interface CheckMinMax_input{
      /**  Minimum range to validate  */  
   ipMinRange:string,
      /**  Maximum range to validate  */  
   ipMaxRange:string,
      /**  COA Code  */  
   ipCOACode:string,
      /**  Segment Number to validate  */  
   ipSegmentNbr:number,
}

export interface CheckMinMax_output{
}

   /** Required : 
      @param ipParamName
   */  
export interface CheckParamName_input{
      /**  Proposed parameter name  */  
   ipParamName:string,
}

export interface CheckParamName_output{
}

   /** Required : 
      @param ipParamOpt
      @param ds
   */  
export interface CheckParamOptionBAQ_input{
   ipParamOpt:number,
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface CheckParamOptionBAQ_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ipAllocID
      @param ipParamNbr
      @param ipSrcSeqNbr
      @param ipParamOpt
      @param ds
   */  
export interface CheckParamOption_input{
   ipAllocID:string,
   ipParamNbr:number,
   ipSrcSeqNbr:number,
   ipParamOpt:number,
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface CheckParamOption_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ipParamSegmentNbr
      @param ipParamType
      @param ds
   */  
export interface CheckParamSegment_input{
   ipParamSegmentNbr:number,
   ipParamType:string,
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface CheckParamSegment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ipAllocID
      @param ipProposedPercentage
   */  
export interface CheckPercentageToAllocate_input{
   ipAllocID:string,
   ipProposedPercentage:number,
}

export interface CheckPercentageToAllocate_output{
parameters : {
      /**  output parameters  */  
   opWarnMsg:string,
}
}

   /** Required : 
      @param ipPriorTgtStamp
      @param ds
   */  
export interface CheckPriorTgtStamp_input{
   ipPriorTgtStamp:string,
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface CheckPriorTgtStamp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
   opWarningMsg:string,
}
}

   /** Required : 
      @param ipAllocID
      @param ipParamNbr
      @param ipSegmentNbr
   */  
export interface CheckSegmentNbr_input{
      /**  Allocation ID  */  
   ipAllocID:string,
      /**  Parameter Number  */  
   ipParamNbr:number,
      /**  Proposed Segment Number  */  
   ipSegmentNbr:number,
}

export interface CheckSegmentNbr_output{
}

   /** Required : 
      @param ipAllocID
      @param ipFormula
   */  
export interface CheckSyntax_input{
      /**  AllocID of selected record  */  
   ipAllocID:string,
      /**  Formula to validate  */  
   ipFormula:string,
}

export interface CheckSyntax_output{
}

   /** Required : 
      @param ipTgtStamp
      @param ds
   */  
export interface CheckTgtStamp_input{
   ipTgtStamp:string,
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface CheckTgtStamp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
   opWarningMsg:string,
}
}

   /** Required : 
      @param ipTier
      @param ds
   */  
export interface CheckTier_input{
   ipTier:number,
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface CheckTier_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ipProposedPercent
      @param ds
   */  
export interface CheckTotalPercent_input{
   ipProposedPercent:number,
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface CheckTotalPercent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
   opTotalPercent:number,
}
}

   /** Required : 
      @param ipAllocID
      @param ipParamNbr
      @param ds
   */  
export interface CreateAlcNFSrcRecords_input{
      /**  GL Allocations Id  */  
   ipAllocID:string,
      /**  Parameter number  */  
   ipParamNbr:number,
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface CreateAlcNFSrcRecords_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param allocID
   */  
export interface DeleteByID_input{
   allocID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_AlcAcctCatRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**   Intended for internal use only to keep the records unique.  The ParamNbr value is 0  when tied to a source account (AlcHed).
When tied to a parameter criteria (AlcParams) it inherits its value from AlcParams table.  */  
   ParamNbr:number,
      /**  Unique identifier of this category of accounts.  */  
   CategoryID:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   AlcAcctCatCOAActCatType:string,
   AlcAcctCatCOAActCatDescription:string,
   COADescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcAcctRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**   Intended for internal use only to keep the records unique.  The ParamNbr value is 0  when tied to a source account (AlcHed).
When tied to a parameter criteria (AlcParams) it inherits its value from AlcParams table.  */  
   ParamNbr:number,
      /**  GL Account or GL Account mask  */  
   AllocGLAcct:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Allocation Segment Value 1  */  
   AllocSegValue1:string,
      /**  Allocation Segment Value 2  */  
   AllocSegValue2:string,
      /**  Allocation Segment Value 3  */  
   AllocSegValue3:string,
      /**  Allocation Segment Value 4  */  
   AllocSegValue4:string,
      /**  Allocation Segment Value 5  */  
   AllocSegValue5:string,
      /**  Allocation Segment Value 6  */  
   AllocSegValue6:string,
      /**  Allocation Segment Value 7  */  
   AllocSegValue7:string,
      /**  Allocation Segment Value 8  */  
   AllocSegValue8:string,
      /**  Allocation Segment Value 9  */  
   AllocSegValue9:string,
      /**  Allocation Segment Value 10  */  
   AllocSegValue10:string,
      /**  Allocation Segment Value 11  */  
   AllocSegValue11:string,
      /**  Allocation Segment Value 12  */  
   AllocSegValue12:string,
      /**  Allocation Segment Value 13  */  
   AllocSegValue13:string,
      /**  Allocation Segment Value 14  */  
   AllocSegValue14:string,
      /**  Allocation Segment Value 15  */  
   AllocSegValue15:string,
      /**  Allocation Segment Value 16  */  
   AllocSegValue16:string,
      /**  Allocation Segment Value 17  */  
   AllocSegValue17:string,
      /**  Allocation Segment Value 18  */  
   AllocSegValue18:string,
      /**  Allocation Segment Value 19  */  
   AllocSegValue19:string,
      /**  Allocation Segment Value 20  */  
   AllocSegValue20:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   COADescription:string,
   GLAcctDispGLAcctDisp:string,
   GLAcctDispGLShortAcct:string,
   GLAcctDispAccountDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcHedListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  Allocation code description.  */  
   Description:string,
      /**   Identifies whether or not the allocaiton is balance or transaction based.  1 = Transaction and is the default value.
2 = Balance based.  */  
   AllocationType:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Allocation tier.  */  
   Tier:number,
      /**  Identifies the allocation stamp to which this allocation is to be applied.  */  
   PriorTgtStamp:string,
      /**  Identifies the allocation stamp that is to to be stamped on the GLJrnDtls.  */  
   TgtStamp:string,
      /**  Identifies the allocation stamp that was processed by this allocation.  */  
   SrcAllocStamp:string,
      /**  When Yes the Allocation Engine ignores the allocation stamp assigned to the GLJrnDtl when determining if a entry is subject to allocations for the current allocation code.  */  
   IgnoreStamp:boolean,
      /**  Yes indicates that all allocation stamps are valid for the allocation code.  */  
   UseAllStamps:boolean,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  */  
   AllocOption:number,
      /**  Postive, fractional value indicating how much of a source is allocated.  Default value is 100.00.  */  
   PercentToAlloc:number,
      /**  Indicates if the allocation units are used.  */  
   UseAllocUnits:boolean,
      /**  The general ledger account the allocation is to be written off.  */  
   OffsetAcct:string,
      /**  Offset Segment Value 1  */  
   OffsetSegVal1:string,
      /**  Offset Segment Value 2  */  
   OffsetSegVal2:string,
      /**  Offset Segment Value 3  */  
   OffsetSegVal3:string,
      /**  Offset Segment Value 4  */  
   OffsetSegVal4:string,
      /**  Offset Segment Value 5  */  
   OffsetSegVal5:string,
      /**  Offset Segment Value 6  */  
   OffsetSegVal6:string,
      /**  Offset Segment Value 7  */  
   OffsetSegVal7:string,
      /**  Offset Segment Value 8  */  
   OffsetSegVal8:string,
      /**  Offset Segment Value 9  */  
   OffsetSegVal9:string,
      /**  Offset Segment Value 10  */  
   OffsetSegVal10:string,
      /**  Offset Segment Value 11  */  
   OffsetSegVal11:string,
      /**  Offset Segment Value 12  */  
   OffsetSegVal12:string,
      /**  Offset Segment Value 13  */  
   OffsetSegVal13:string,
      /**  Offset Segment Value 14  */  
   OffsetSegVal14:string,
      /**  Offset Segment Value 15  */  
   OffsetSegVal15:string,
      /**  Offset Segment Value 16  */  
   OffsetSegVal16:string,
      /**  Offset Segment Value 17  */  
   OffsetSegVal17:string,
      /**  Offset Segment Value 18  */  
   OffsetSegVal18:string,
      /**  Offset Segment Value 19  */  
   OffsetSegVal19:string,
      /**  Offset Segment Value 20  */  
   OffsetSegVal20:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates whether or not a allocation is currently executing.  */  
   AllocIsRunning:boolean,
      /**  Total allocation units.  This is the sum of the allocation units defined on the targets.  */  
   TotalAllocUnits:number,
      /**  his is the sum of the percentage values defined on the targets.  */  
   TotalPercentage:number,
   OffsetAcctDesc:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   GLAcctDispGLAcctDisp:string,
      /**  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The value of this field is the concatenation of the first three controlled display order segments.  For example, if a chart has 5 controlled segments that are displayed in the following order: seg5->seg3->seg4->seg2->seg1, this field contains the concatention of seg5->seg3->seg4 up to th  */  
   GLAcctDispGLShortAcct:string,
      /**  Text that describes the account.  */  
   GLAcctDispAccountDesc:string,
      /**  Descripiton of Book  */  
   GLBookDescription:string,
      /**  Indicates the base currency for the book  */  
   GLBookCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcHedListTableset{
   AlcHedList:Erp_Tablesets_AlcHedListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_AlcHedRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  Allocation code description.  */  
   Description:string,
      /**   Identifies whether or not the allocaiton is balance or transaction based.  1 = Transaction and is the default value.
2 = Balance based.  */  
   AllocationType:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Allocation tier.  */  
   Tier:number,
      /**  Identifies the allocation stamp to which this allocation is to be applied.  */  
   PriorTgtStamp:string,
      /**  Identifies the allocation stamp that is to to be stamped on the GLJrnDtls.  */  
   TgtStamp:string,
      /**  Identifies the allocation stamp that was processed by this allocation.  */  
   SrcAllocStamp:string,
      /**  When Yes the Allocation Engine ignores the allocation stamp assigned to the GLJrnDtl when determining if a entry is subject to allocations for the current allocation code.  */  
   IgnoreStamp:boolean,
      /**  Yes indicates that all allocation stamps are valid for the allocation code.  */  
   UseAllStamps:boolean,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  */  
   AllocOption:number,
      /**  Postive, fractional value indicating how much of a source is allocated.  Default value is 100.00.  */  
   PercentToAlloc:number,
      /**  Indicates if the allocation units are used.  */  
   UseAllocUnits:boolean,
      /**  The general ledger account the allocation is to be written off.  */  
   OffsetAcct:string,
      /**  Offset Segment Value 1  */  
   OffsetSegVal1:string,
      /**  Offset Segment Value 2  */  
   OffsetSegVal2:string,
      /**  Offset Segment Value 3  */  
   OffsetSegVal3:string,
      /**  Offset Segment Value 4  */  
   OffsetSegVal4:string,
      /**  Offset Segment Value 5  */  
   OffsetSegVal5:string,
      /**  Offset Segment Value 6  */  
   OffsetSegVal6:string,
      /**  Offset Segment Value 7  */  
   OffsetSegVal7:string,
      /**  Offset Segment Value 8  */  
   OffsetSegVal8:string,
      /**  Offset Segment Value 9  */  
   OffsetSegVal9:string,
      /**  Offset Segment Value 10  */  
   OffsetSegVal10:string,
      /**  Offset Segment Value 11  */  
   OffsetSegVal11:string,
      /**  Offset Segment Value 12  */  
   OffsetSegVal12:string,
      /**  Offset Segment Value 13  */  
   OffsetSegVal13:string,
      /**  Offset Segment Value 14  */  
   OffsetSegVal14:string,
      /**  Offset Segment Value 15  */  
   OffsetSegVal15:string,
      /**  Offset Segment Value 16  */  
   OffsetSegVal16:string,
      /**  Offset Segment Value 17  */  
   OffsetSegVal17:string,
      /**  Offset Segment Value 18  */  
   OffsetSegVal18:string,
      /**  Offset Segment Value 19  */  
   OffsetSegVal19:string,
      /**  Offset Segment Value 20  */  
   OffsetSegVal20:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if Statistical Balance of Target Account should be used as Allocation Units  */  
   StatBalAsAllocUnits:boolean,
      /**  Indicates whether or not a allocation is currently executing.  */  
   AllocIsRunning:boolean,
      /**  Total allocation units.  This is the sum of the allocation units defined on the targets.  */  
   TotalAllocUnits:number,
      /**  his is the sum of the percentage values defined on the targets.  */  
   TotalPercentage:number,
   OffsetAcctDesc:string,
   BitFlag:number,
   GLAcctDispGLAcctDisp:string,
   GLAcctDispAccountDesc:string,
   GLAcctDispGLShortAcct:string,
   GLBookDescription:string,
   GLBookCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcHedTableset{
   AlcHed:Erp_Tablesets_AlcHedRow[],
   AlcAcct:Erp_Tablesets_AlcAcctRow[],
   AlcAcctCat:Erp_Tablesets_AlcAcctCatRow[],
   AlcJrnCd:Erp_Tablesets_AlcJrnCdRow[],
   AlcParams:Erp_Tablesets_AlcParamsRow[],
   AlcNFSrc:Erp_Tablesets_AlcNFSrcRow[],
   AlcParamsBAQ:Erp_Tablesets_AlcParamsBAQRow[],
   AlcRange:Erp_Tablesets_AlcRangeRow[],
   AlcTarget:Erp_Tablesets_AlcTargetRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_AlcJrnCdRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**   Intended for internal use only to keep the records unique.  The ParamNbr value is 0  when tied to a source account (AlcHed).
When tied to a parameter criteria (AlcParams) it inherits its value from AlcParams table.  */  
   ParamNbr:number,
      /**  Unique identifier of the journal used to group entries. The user can create their own journal codes to be used instead of the default codes.  */  
   JournalCode:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   JrnlCodeJrnlDescription:string,
   JrnlCodeSystemJournal:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcNFSrcRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  Intended for internal use only to keep the records unique.  The value is inherited from the AlcParams table.  */  
   ParamNbr:number,
      /**  LookupTblMapUID_obsolete  */  
   LookupTblMapUID_obsolete:number,
      /**  TgtSeqNbr_obsolete  */  
   TgtSeqNbr_obsolete:number,
      /**  LinkUID_obsolete  */  
   LinkUID_obsolete:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**   Identifes the option for the BAQ parameter.
1 = Use Target Account Segment.  
2 = Use Source Account Segment
3 = Use Allocation Run Start Date
4 = Use allocation Run End Date  */  
   ParamOpt:number,
      /**  Identifies the segment number to use to determine the segment code that will be used to look up the result value in the lookup table.  */  
   ParamSegmentNbr:number,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Identifies if the parameter is an actual value or an option.  */  
   EntryType:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  SrcSeqNbr  */  
   SrcSeqNbr:number,
      /**  SrcCodeID  */  
   SrcCodeID:string,
      /**  List of LookupLink records for the cmbLinkUID combo  */  
   LinkList:string,
      /**  Source Field Link Description (Summ of Lookup Link Field1 to Field30 and Value1 to Value30 information)  */  
   SrcFieldDesc:string,
   SrcFieldName:string,
   DspSrcCodeID:string,
   SrcDataType:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcParamsBAQRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  Intended for internal use only to keep the records unique.  */  
   ParamNbr:number,
      /**  Intended for internal use only to keep the records unique.  */  
   BAQParamValNbr:number,
      /**  BAQ ID, the unique identifier for this Query table within the company  */  
   BAQExportID:string,
   ParameterName:string,
      /**  Specific baq parameter value.  */  
   BAQParamCode:string,
      /**   Identifes the option for the BAQ parameter.
1 = Use Target Account Segment.  
2 = Use Source Account Segment
3 = Use Allocation Run Start Date
4 = Use allocation Run End Date  */  
   ParamOpt:number,
      /**  Identifies the segment number to use to determine the segment code that will be used to look up the result value in the lookup table.  */  
   ParamSegmentNbr:number,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Identifies if the parameter is an actual value or an option.  */  
   EntryType:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   ParamSegmentName:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcParamsRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  Intended for internal use only to keep the records unique.  */  
   ParamNbr:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  The name assigned to a parameter.  This name must be unique.  */  
   ParamName:string,
      /**  Identifies the type of parameter used in the allocation logic.  1 = Account Balances, 2 = Summarized balances,  3 = BAQ and 4 = Non Financial Data.  */  
   ParamType:number,
      /**  Text that describes the parameter.  */  
   ParamDesc:string,
      /**  Indicates the source data for the value of a parameter value when the parameter is of type Account Balance.  */  
   AcctParamValSrc:number,
      /**  Indicates the source data for the value of a parameter value when the parameter is of type Summarized.  */  
   SumParamValSrc:number,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Account balance account.  Only valid when the formula type = 1.  */  
   AcctBalAcct:string,
      /**  Account Segment Value 1  */  
   AcctBalSegVal1:string,
      /**  Account Segment Value 2  */  
   AcctBalSegVal2:string,
      /**  Account Segment Value 3  */  
   AcctBalSegVal3:string,
      /**  Account Segment Value 4  */  
   AcctBalSegVal4:string,
      /**  Account Segment Value 5  */  
   AcctBalSegVal5:string,
      /**  Account Segment Value 6  */  
   AcctBalSegVal6:string,
      /**  Account Segment Value 7  */  
   AcctBalSegVal7:string,
      /**  Account Segment Value 8  */  
   AcctBalSegVal8:string,
      /**  Account Segment Value 9  */  
   AcctBalSegVal9:string,
      /**  Account Segment Value 10  */  
   AcctBalSegVal10:string,
      /**  Account Segment Value 11  */  
   AcctBalSegVal11:string,
      /**  Account Segment Value 12  */  
   AcctBalSegVal12:string,
      /**  Account Segment Value 13  */  
   AcctBalSegVal13:string,
      /**  Account Segment Value 14  */  
   AcctBalSegVal14:string,
      /**  Account Segment Value 15  */  
   AcctBalSegVal15:string,
      /**  Account Segment Value 16  */  
   AcctBalSegVal16:string,
      /**  Account Segment Value 17  */  
   AcctBalSegVal17:string,
      /**  Account Segment Value 18  */  
   AcctBalSegVal18:string,
      /**  Account Segment Value 19  */  
   AcctBalSegVal19:string,
      /**  Account Segment Value 20  */  
   AcctBalSegVal20:string,
      /**  Yes indictes the target account's balance is taken and the AcctBalAcct is set equal to the AlcTarget.TgtGLAcct.  This only only valid when the formula type = Account Balances.  */  
   UseTgtAcct:boolean,
      /**  BAQ ID, the unique identifier for this Query table within the company  */  
   BAQExportID:string,
      /**  Statistical UOM code.  */  
   StatUOMCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  NFSrcMapUID  */  
   NFSrcMapUID:number,
      /**  NFTgtSeqNbr  */  
   NFTgtSeqNbr:number,
      /**  YTDBalance  */  
   YTDBalance:boolean,
      /**  Indicates whether or not the BAQ has parameters defined.  If not, then the user cannot define BAQ parameters in allocation code maintenance.  */  
   BAQEnableParams:boolean,
      /**  Dynamic query description  */  
   BAQExportIDDescription:string,
   BitFlag:number,
   GLAcctDispGLShortAcct:string,
   GLAcctDispAccountDesc:string,
   GLAcctDispGLAcctDisp:string,
   GLBookDescription:string,
   GLBookCurrencyCode:string,
   LookupTableIDDisplayName:string,
   TargetFieldNameFieldName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcRangeRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**   Intended for internal use only to keep the records unique.  The ParamNbr value is 0  when tied to a source account (AlcHed).
When tied to a parameter criteria (AlcParams) it inherits its value from AlcParams table.  */  
   ParamNbr:number,
      /**  System generated number from 1 through 20.  */  
   SegmentNbr:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Minimum vale for range selection.  */  
   MinValue:string,
      /**  Maximum value for range selection.  */  
   MaxValue:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   COASegmentSegmentName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcTargetRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   AllocTgtNbr:number,
      /**  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  */  
   AllocOption:number,
      /**  Formula entered by the user used to calculate the allocation amount.  Only valid if the allocation option = 2.  */  
   RatioFormula:string,
      /**  Postive, fractional value indicating how much of an allocation is applied to this target.  */  
   RatioValue:number,
      /**   The relative  number of units used to allocate to this account.
Allocation units / Total Allocation units is used to distribute the amount. Total Allocation units are calculated for a given AllocID and not stored.  */  
   AllocUnits:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  The GL Account an amount is allocated to.  This may be an actual GL Account or a masked account where each mask character is swapped with the corresponding character from the source GL Account.  */  
   TgtGLAcct:string,
      /**  Target Segment Value 1  */  
   TgtSegVal1:string,
      /**  Target Segment Value 2  */  
   TgtSegVal2:string,
      /**  Target Segment Value 3  */  
   TgtSegVal3:string,
      /**  Target Segment Value 4  */  
   TgtSegVal4:string,
      /**  Target Segment Value 5  */  
   TgtSegVal5:string,
      /**  Target Segment Value 6  */  
   TgtSegVal6:string,
      /**  Target Segment Value 7  */  
   TgtSegVal7:string,
      /**  Target Segment Value 8  */  
   TgtSegVal8:string,
      /**  Target Segment Value 9  */  
   TgtSegVal9:string,
      /**  Target Segment Value 10  */  
   TgtSegVal10:string,
      /**  Target Segment Value 11  */  
   TgtSegVal11:string,
      /**  Target Segment Value 12  */  
   TgtSegVal12:string,
      /**  Target Segment Value 13  */  
   TgtSegVal13:string,
      /**  Target Segment Value 14  */  
   TgtSegVal14:string,
      /**  Target Segment Value 15  */  
   TgtSegVal15:string,
      /**  Target Segment Value 16  */  
   TgtSegVal16:string,
      /**  Target Segment Value 17  */  
   TgtSegVal17:string,
      /**  Target Segment Value 18  */  
   TgtSegVal18:string,
      /**  Target Segment Value 19  */  
   TgtSegVal19:string,
      /**  Target Segment Value 20  */  
   TgtSegVal20:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MultiCompany  */  
   MultiCompany:boolean,
      /**  ExtCompanyID  */  
   ExtCompanyID:string,
      /**  ExtGLAccount  */  
   ExtGLAccount:string,
      /**  ExtCOACode  */  
   ExtCOACode:string,
      /**  ExtSegValue1  */  
   ExtSegValue1:string,
      /**  ExtSegValue2  */  
   ExtSegValue2:string,
      /**  ExtSegValue3  */  
   ExtSegValue3:string,
      /**  ExtSegValue4  */  
   ExtSegValue4:string,
      /**  ExtSegValue5  */  
   ExtSegValue5:string,
      /**  ExtSegValue6  */  
   ExtSegValue6:string,
      /**  ExtSegValue7  */  
   ExtSegValue7:string,
      /**  ExtSegValue8  */  
   ExtSegValue8:string,
      /**  ExtSegValue9  */  
   ExtSegValue9:string,
      /**  ExtSegValue10  */  
   ExtSegValue10:string,
      /**  ExtSegValue11  */  
   ExtSegValue11:string,
      /**  ExtSegValue12  */  
   ExtSegValue12:string,
      /**  ExtSegValue13  */  
   ExtSegValue13:string,
      /**  ExtSegValue14  */  
   ExtSegValue14:string,
      /**  ExtSegValue15  */  
   ExtSegValue15:string,
      /**  ExtSegValue16  */  
   ExtSegValue16:string,
      /**  ExtSegValue17  */  
   ExtSegValue17:string,
      /**  ExtSegValue18  */  
   ExtSegValue18:string,
      /**  ExtSegValue19  */  
   ExtSegValue19:string,
      /**  ExtSegValue20  */  
   ExtSegValue20:string,
      /**  OverrideGLAcct  */  
   OverrideGLAcct:boolean,
      /**  Used to bind UI control.  */  
   Argument1:string,
      /**  Used to bind UI control.  */  
   Argument2:string,
      /**  Used to bind UI control.  */  
   Operator:string,
      /**  Target GL Account Description  */  
   TgtGLDesc:string,
      /**  Ext GL Account Description  */  
   ExtAccountDesc:string,
      /**  Flag to indicate if the MultiCompany check box needs to be enabled.  */  
   EnableMultiCompany:boolean,
   BitFlag:number,
   GLAcctDispAccountDesc:string,
   GLAcctDispGLShortAcct:string,
   GLAcctDispGLAcctDisp:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtAlcHedTableset{
   AlcHed:Erp_Tablesets_AlcHedRow[],
   AlcAcct:Erp_Tablesets_AlcAcctRow[],
   AlcAcctCat:Erp_Tablesets_AlcAcctCatRow[],
   AlcJrnCd:Erp_Tablesets_AlcJrnCdRow[],
   AlcParams:Erp_Tablesets_AlcParamsRow[],
   AlcNFSrc:Erp_Tablesets_AlcNFSrcRow[],
   AlcParamsBAQ:Erp_Tablesets_AlcParamsBAQRow[],
   AlcRange:Erp_Tablesets_AlcRangeRow[],
   AlcTarget:Erp_Tablesets_AlcTargetRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param allocID
   */  
export interface GetByID_input{
   allocID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_AlcHedTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_AlcHedTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_AlcHedTableset[],
}

   /** Required : 
      @param ipMapUID
      @param ipSrcSeqNbr
      @param ipWhereClause
   */  
export interface GetLinkList_input{
      /**  Map Unique ID  */  
   ipMapUID:number,
      /**  Src Sequence Number  */  
   ipSrcSeqNbr:number,
      /**  Where Clause  */  
   ipWhereClause:string,
}

export interface GetLinkList_output{
parameters : {
      /**  output parameters  */  
   opLinkList:string,
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
   returnObj:Erp_Tablesets_AlcHedListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipDspSrcCodeID
      @param ipSrcDataType
   */  
export interface GetLookupSrcCodeID_input{
      /**  Display Source Field Code  */  
   ipDspSrcCodeID:string,
      /**  Source Field Code Data Type  */  
   ipSrcDataType:string,
}

export interface GetLookupSrcCodeID_output{
parameters : {
      /**  output parameters  */  
   opSrcCodeID:string,
}
}

   /** Required : 
      @param ds
      @param allocID
      @param paramNbr
   */  
export interface GetNewAlcAcctCat_input{
   ds:Erp_Tablesets_AlcHedTableset[],
   allocID:string,
   paramNbr:number,
}

export interface GetNewAlcAcctCat_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ds
      @param allocID
      @param paramNbr
   */  
export interface GetNewAlcAcct_input{
   ds:Erp_Tablesets_AlcHedTableset[],
   allocID:string,
   paramNbr:number,
}

export interface GetNewAlcAcct_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewAlcHed_input{
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface GetNewAlcHed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ds
      @param allocID
      @param paramNbr
   */  
export interface GetNewAlcJrnCd_input{
   ds:Erp_Tablesets_AlcHedTableset[],
   allocID:string,
   paramNbr:number,
}

export interface GetNewAlcJrnCd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ipAllocID
      @param ipParamNbr
      @param ds
   */  
export interface GetNewAlcNFSrc1_input{
      /**  Allocation ID  */  
   ipAllocID:string,
      /**  Parameter Number  */  
   ipParamNbr:number,
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface GetNewAlcNFSrc1_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ds
      @param allocID
      @param paramNbr
   */  
export interface GetNewAlcNFSrc_input{
   ds:Erp_Tablesets_AlcHedTableset[],
   allocID:string,
   paramNbr:number,
}

export interface GetNewAlcNFSrc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ds
      @param allocID
      @param paramNbr
      @param baQExportID
   */  
export interface GetNewAlcParamsBAQ_input{
   ds:Erp_Tablesets_AlcHedTableset[],
   allocID:string,
   paramNbr:number,
   baQExportID:string,
}

export interface GetNewAlcParamsBAQ_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ds
      @param allocID
   */  
export interface GetNewAlcParams_input{
   ds:Erp_Tablesets_AlcHedTableset[],
   allocID:string,
}

export interface GetNewAlcParams_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ipAllocID
      @param ipParamNbr
      @param ipCOACode
      @param ds
   */  
export interface GetNewAlcRange1_input{
      /**  Allocation ID  */  
   ipAllocID:string,
      /**  Parameter Number  */  
   ipParamNbr:number,
      /**  COA Code  */  
   ipCOACode:string,
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface GetNewAlcRange1_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ds
      @param allocID
      @param paramNbr
   */  
export interface GetNewAlcRange_input{
   ds:Erp_Tablesets_AlcHedTableset[],
   allocID:string,
   paramNbr:number,
}

export interface GetNewAlcRange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ds
      @param allocID
   */  
export interface GetNewAlcTarget_input{
   ds:Erp_Tablesets_AlcHedTableset[],
   allocID:string,
}

export interface GetNewAlcTarget_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

export interface GetOperatorsList_output{
parameters : {
      /**  output parameters  */  
   opOperatorsList:string,
}
}

export interface GetOperatorsMenuList_output{
parameters : {
      /**  output parameters  */  
   opMenuItem:string,
}
}

   /** Required : 
      @param ipAllocID
   */  
export interface GetParamMenuList_input{
      /**  Allocation ID  */  
   ipAllocID:string,
}

export interface GetParamMenuList_output{
parameters : {
      /**  output parameters  */  
   opMenuItem:string,
}
}

   /** Required : 
      @param ipAllocID
   */  
export interface GetParametersList_input{
      /**  Allocation ID  */  
   ipAllocID:string,
}

export interface GetParametersList_output{
parameters : {
      /**  output parameters  */  
   opParametersList:string,
}
}

   /** Required : 
      @param whereClauseAlcHed
      @param whereClauseAlcAcct
      @param whereClauseAlcAcctCat
      @param whereClauseAlcJrnCd
      @param whereClauseAlcParams
      @param whereClauseAlcNFSrc
      @param whereClauseAlcParamsBAQ
      @param whereClauseAlcRange
      @param whereClauseAlcTarget
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseAlcHed:string,
   whereClauseAlcAcct:string,
   whereClauseAlcAcctCat:string,
   whereClauseAlcJrnCd:string,
   whereClauseAlcParams:string,
   whereClauseAlcNFSrc:string,
   whereClauseAlcParamsBAQ:string,
   whereClauseAlcRange:string,
   whereClauseAlcTarget:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_AlcHedTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
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
      @param tableName
      @param glAccount
      @param mask
      @param ds
   */  
export interface MaskValidate_input{
      /**  Table name the tested account belongs to  */  
   tableName:string,
      /**  GL account  */  
   glAccount:string,
      /**  Mask symbol '_' or '%'  */  
   mask:string,
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface MaskValidate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface RefreshAllocationTotals_input{
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface RefreshAllocationTotals_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ipType
      @param ds
   */  
export interface RetrieveGLAcctDesc_input{
   ipType:string,
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface RetrieveGLAcctDesc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ipUseTgtAcct
      @param ds
   */  
export interface UpdateAcctBalAcct_input{
      /**  Use Target Account field value  */  
   ipUseTgtAcct:boolean,
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface UpdateAcctBalAcct_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtAlcHedTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtAlcHedTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ipAllocID
      @param ipParamNbr
      @param ipSegment
   */  
export interface ValidParamNatSegment_input{
   ipAllocID:string,
   ipParamNbr:number,
   ipSegment:string,
}

export interface ValidParamNatSegment_output{
parameters : {
      /**  output parameters  */  
   opWarnMsg:string,
}
}

   /** Required : 
      @param ipAllocID
      @param ipSegment
   */  
export interface ValidTgtNatSegment_input{
   ipAllocID:string,
   ipSegment:string,
}

export interface ValidTgtNatSegment_output{
parameters : {
      /**  output parameters  */  
   opWarnMsg:string,
}
}

   /** Required : 
      @param ipAllocID
   */  
export interface ValidatePercentTotals_input{
   ipAllocID:string,
}

export interface ValidatePercentTotals_output{
parameters : {
      /**  output parameters  */  
   opWarnMsg:string,
}
}

   /** Required : 
      @param ipBAQExportID
      @param ipAllocID
      @param ipParamNbr
      @param ds
   */  
export interface createNewBAQParams_input{
   ipBAQExportID:string,
   ipAllocID:string,
   ipParamNbr:number,
   ds:Erp_Tablesets_AlcHedTableset[],
}

export interface createNewBAQParams_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTableset[],
}
}

   /** Required : 
      @param ProposedExtCompID
   */  
export interface getExternalMasterCOA_input{
   ProposedExtCompID:string,
}

export interface getExternalMasterCOA_output{
   returnObj:string,
}

