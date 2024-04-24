import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.BankAcctSvc
// Description: bo/BankAcct/BankAcct.p
           BankAcct Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/$metadata", {
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
   Description: Get BankAccts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankAccts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankAcctRow
   */  
export function get_BankAccts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankAccts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankAcctRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BankAcctRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BankAccts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts", {
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
   Summary: Calls GetByID to retrieve the BankAcct item
   Description: Calls GetByID to retrieve the BankAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankAcctRow
   */  
export function get_BankAccts_Company_BankAcctID(Company:string, BankAcctID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts(" + Company + "," + BankAcctID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_BankAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BankAcct for the service
   Description: Calls UpdateExt to update BankAcct. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankAcctRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BankAccts_Company_BankAcctID(Company:string, BankAcctID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts(" + Company + "," + BankAcctID + ")", {
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
   Summary: Call UpdateExt to delete BankAcct item
   Description: Call UpdateExt to delete BankAcct item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BankAccts_Company_BankAcctID(Company:string, BankAcctID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts(" + Company + "," + BankAcctID + ")", {
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
   Description: Get BankPayMethods items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BankPayMethods1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankPayMethodRow
   */  
export function get_BankAccts_Company_BankAcctID_BankPayMethods(Company:string, BankAcctID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankPayMethodRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts(" + Company + "," + BankAcctID + ")/BankPayMethods", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankPayMethodRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BankPayMethod item
   Description: Calls GetByID to retrieve the BankPayMethod item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankPayMethod1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param PMUID Desc: PMUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankPayMethodRow
   */  
export function get_BankAccts_Company_BankAcctID_BankPayMethods_Company_BankAcctID_PMUID(Company:string, BankAcctID:string, PMUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankPayMethodRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts(" + Company + "," + BankAcctID + ")/BankPayMethods(" + Company + "," + BankAcctID + "," + PMUID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_BankPayMethodRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get Partners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_Partners1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
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
export function get_BankAccts_Company_BankAcctID_Partners(Company:string, BankAcctID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartnerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts(" + Company + "," + BankAcctID + ")/Partners", {
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
   Summary: Calls GetByID to retrieve the Partner item
   Description: Calls GetByID to retrieve the Partner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Partner1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
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
export function get_BankAccts_Company_BankAcctID_Partners_Company_PartnerNum_PartnerType_PartnerID_SearchID(Company:string, BankAcctID:string, PartnerNum:string, PartnerType:string, PartnerID:string, SearchID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartnerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts(" + Company + "," + BankAcctID + ")/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")", {
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
   Summary: Calls GetByID for the service
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
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
export function get_BankAccts_Company_BankAcctID_EntityGLCs(Company:string, BankAcctID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts(" + Company + "," + BankAcctID + ")/EntityGLCs", {
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
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
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
export function get_BankAccts_Company_BankAcctID_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, BankAcctID:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts(" + Company + "," + BankAcctID + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Description: Get BankAcctAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BankAcctAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankAcctAttchRow
   */  
export function get_BankAccts_Company_BankAcctID_BankAcctAttches(Company:string, BankAcctID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankAcctAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts(" + Company + "," + BankAcctID + ")/BankAcctAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankAcctAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BankAcctAttch item
   Description: Calls GetByID to retrieve the BankAcctAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankAcctAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankAcctAttchRow
   */  
export function get_BankAccts_Company_BankAcctID_BankAcctAttches_Company_BankAcctID_DrawingSeq(Company:string, BankAcctID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankAcctAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts(" + Company + "," + BankAcctID + ")/BankAcctAttches(" + Company + "," + BankAcctID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_BankAcctAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get BankPayMethods items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankPayMethods
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankPayMethodRow
   */  
export function get_BankPayMethods(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankPayMethodRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankPayMethods", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankPayMethodRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankPayMethods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankPayMethodRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BankPayMethodRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BankPayMethods(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankPayMethods", {
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
   Summary: Calls GetByID to retrieve the BankPayMethod item
   Description: Calls GetByID to retrieve the BankPayMethod item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankPayMethod
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param PMUID Desc: PMUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankPayMethodRow
   */  
export function get_BankPayMethods_Company_BankAcctID_PMUID(Company:string, BankAcctID:string, PMUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankPayMethodRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankPayMethods(" + Company + "," + BankAcctID + "," + PMUID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_BankPayMethodRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BankPayMethod for the service
   Description: Calls UpdateExt to update BankPayMethod. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankPayMethod
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param PMUID Desc: PMUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankPayMethodRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BankPayMethods_Company_BankAcctID_PMUID(Company:string, BankAcctID:string, PMUID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankPayMethods(" + Company + "," + BankAcctID + "," + PMUID + ")", {
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
   Summary: Call UpdateExt to delete BankPayMethod item
   Description: Call UpdateExt to delete BankPayMethod item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankPayMethod
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param PMUID Desc: PMUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BankPayMethods_Company_BankAcctID_PMUID(Company:string, BankAcctID:string, PMUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankPayMethods(" + Company + "," + BankAcctID + "," + PMUID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/Partners", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/Partners", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/EntityGLCs", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/EntityGLCs", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Description: Get BankAcctAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankAcctAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankAcctAttchRow
   */  
export function get_BankAcctAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankAcctAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAcctAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankAcctAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankAcctAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankAcctAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BankAcctAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BankAcctAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAcctAttches", {
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
   Summary: Calls GetByID to retrieve the BankAcctAttch item
   Description: Calls GetByID to retrieve the BankAcctAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankAcctAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankAcctAttchRow
   */  
export function get_BankAcctAttches_Company_BankAcctID_DrawingSeq(Company:string, BankAcctID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BankAcctAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAcctAttches(" + Company + "," + BankAcctID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_BankAcctAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BankAcctAttch for the service
   Description: Calls UpdateExt to update BankAcctAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankAcctAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankAcctAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BankAcctAttches_Company_BankAcctID_DrawingSeq(Company:string, BankAcctID:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAcctAttches(" + Company + "," + BankAcctID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete BankAcctAttch item
   Description: Call UpdateExt to delete BankAcctAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankAcctAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BankAcctID Desc: BankAcctID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BankAcctAttches_Company_BankAcctID_DrawingSeq(Company:string, BankAcctID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAcctAttches(" + Company + "," + BankAcctID + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankAcctListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankAcctListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankAcctListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseBankAcct:string, whereClauseBankAcctAttch:string, whereClauseBankPayMethod:string, whereClausePartner:string, whereClauseEntityGLC:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseBankAcct!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBankAcct=" + whereClauseBankAcct
   }
   if(typeof whereClauseBankAcctAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBankAcctAttch=" + whereClauseBankAcctAttch
   }
   if(typeof whereClauseBankPayMethod!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBankPayMethod=" + whereClauseBankPayMethod
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
   if(typeof whereClauseEntityGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEntityGLC=" + whereClauseEntityGLC
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/GetRows" + params, {
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
export function get_GetByID(bankAcctID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof bankAcctID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "bankAcctID=" + bankAcctID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/GetByID" + params, {
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
   Summary: Invoke method ChangeBankBranchCode
   Description: Check if the Bank Branch code changed.
   OperationID: ChangeBankBranchCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBankBranchCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBankBranchCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeBankBranchCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/ChangeBankBranchCode", {
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
   Summary: Invoke method ChangeDebNoteOnly
   Description: Check if the Bank DebNoteOnly flag could be changed.
   OperationID: ChangeDebNoteOnly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDebNoteOnly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDebNoteOnly_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDebNoteOnly(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/ChangeDebNoteOnly", {
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
   Summary: Invoke method ChangeLOCLimit
   Description: Method to call when changing the Limit of Credit amount on an Bank record.  Updates BankAcct
amounts based on the new Limit of Credit amount.
   OperationID: ChangeLOCLimit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLOCLimit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLOCLimit_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeLOCLimit(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/ChangeLOCLimit", {
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
   Summary: Invoke method CheckBankCustNum
   Description: Check Bank Customer Number
At this time this method is specific to Switzerland localization
   OperationID: CheckBankCustNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBankCustNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBankCustNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckBankCustNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/CheckBankCustNum", {
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
   Summary: Invoke method CheckISRPartyID
   Description: Check ISR Party ID
At this time this method is specific to Switzerland localization
   OperationID: CheckISRPartyID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckISRPartyID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckISRPartyID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckISRPartyID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/CheckISRPartyID", {
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
   Summary: Invoke method GetAPLOCClosed
   Description: This method will retrieve information about Letter of Credit with status Closed
   OperationID: GetAPLOCClosed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAPLOCClosed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAPLOCClosed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAPLOCClosed(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/GetAPLOCClosed", {
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
   Summary: Invoke method GetAPLOCOpen
   Description: This method will retrieve information about Letter of Credit with status Open
   OperationID: GetAPLOCOpen
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAPLOCOpen_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAPLOCOpen_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAPLOCOpen(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/GetAPLOCOpen", {
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
   Summary: Invoke method GetBankBal
   Description: Get bank balance.
   OperationID: GetBankBal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBankBal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankBal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBankBal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/GetBankBal", {
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
   Summary: Invoke method GetBankBalFromDate
   Description: Get bank balance from a date. First we need to get the fiscal year that has that particular date in range and then get the balance for that fiscal year.
   OperationID: GetBankBalFromDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBankBalFromDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankBalFromDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBankBalFromDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/GetBankBalFromDate", {
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
   Summary: Invoke method GetCurrencyBase
   Description: This method returns the Base Currency
   OperationID: GetCurrencyBase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyBase_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrencyBase(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/GetCurrencyBase", {
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
   Summary: Invoke method GetBaseCurrencySymbol
   OperationID: GetBaseCurrencySymbol
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBaseCurrencySymbol_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBaseCurrencySymbol(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/GetBaseCurrencySymbol", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/GetCodeDescList", {
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
   Summary: Invoke method GetRowsForMandate
   Description: Returns BankAcct records, for which Creditor ID is not empty.
   OperationID: GetRowsForMandate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForMandate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForMandate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForMandate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/GetRowsForMandate", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/ModifySearchIDs", {
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
   Summary: Invoke method ValidatePartner
   Description: validate PartnerID
   OperationID: ValidatePartner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePartner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePartner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePartner(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/ValidatePartner", {
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
   Summary: Invoke method GetEnableMICR
   Description: Return EnableMICR as true when theres at least one MICR Payment
   OperationID: GetEnableMICR
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEnableMICR_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEnableMICR_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEnableMICR(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/GetEnableMICR", {
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
   Summary: Invoke method GetNewBankAcct
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBankAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBankAcct(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/GetNewBankAcct", {
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
   Summary: Invoke method GetNewBankAcctAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBankAcctAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankAcctAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankAcctAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBankAcctAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/GetNewBankAcctAttch", {
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
   Summary: Invoke method GetNewBankPayMethod
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBankPayMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankPayMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankPayMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBankPayMethod(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/GetNewBankPayMethod", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/GetNewPartner", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/GetNewEntityGLC", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/GetList" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankAcctAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BankAcctAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankAcctListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BankAcctListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankAcctRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BankAcctRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankPayMethodRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BankPayMethodRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EntityGLCRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartnerRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartnerRow[],
}

export interface Erp_Tablesets_BankAcctAttchRow{
   "Company":string,
   "BankAcctID":string,
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

export interface Erp_Tablesets_BankAcctListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of the bank account assigned by the user.  */  
   "BankAcctID":string,
      /**  Full description of the bank account.  */  
   "Description":string,
      /**  The account number for the bank account. Used for reference only.  */  
   "CheckingAccount":string,
      /**  Indicates whether or not the bank account is an active account.  */  
   "Closed":boolean,
      /**  Swift Number or ABA Routing Number  */  
   "BankIdentifier":string,
      /**  IBAN Code  */  
   "IBANCode":string,
      /**  Use the bank average value as the rate for payments from this account.  */  
   "APPaymentUseBankAvg":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates of bank account that now have an open statement waiting to be finally matched/posted.  */  
   "OpenStatement":boolean,
      /**  PositivePayRemoteID  */  
   "PositivePayRemoteID":string,
      /**  PositivePayBatchID  */  
   "PositivePayBatchID":string,
      /**  DefPosPayEFTHeadUID  */  
   "DefPosPayEFTHeadUID":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_BankAcctRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of the bank account assigned by the user.  */  
   "BankAcctID":string,
      /**  Full description of the bank account.  */  
   "Description":string,
      /**  The account number for the bank account. Used for reference only.  */  
   "CheckingAccount":string,
      /**  Indicates whether or not the bank account is an active account.  */  
   "Closed":boolean,
      /**  The Opening Balance of the Bank Account. When a bank reconciliation is posted, this field is set to the posted reconciliation's closing balance and becomes the opening balance for the next statement.  */  
   "OpeningBalance":number,
      /**  The Opening Date of the Bank Account.  When a bank reconciliation is posted, the next statement's opening date is set to the posted reconciliation's Closing Date + 1 and becomes the opening date for the next statement.  */  
   "OpeningDate":string,
      /**  The Closing Balance of the Bank Account. When a bank reconciliation is posted, this field is set to the posted reconciliation's closing balance.  */  
   "ClosingBalance":number,
      /**  The Closing Date of the Bank Account. When a bank reconciliation is posted, this field is set to the posted reconciliation's closing date.  */  
   "ClosingDate":string,
      /**  The bank's routing number.  */  
   "BankRoutingNum":string,
      /**  The check digit for the bank.  */  
   "BankCheckDigit":number,
      /**  The Bank's full name.  */  
   "BankName":string,
      /**   Service Class Code 200 = Mixed debit or credit entries and pre-notification entries.

Contact your bank for the appropriate value.  */  
   "ServClassCode":string,
      /**   PPD - Prearranged Payments and Deposits for consumer items.
CCD - Cash concentration and disbursements for non-consumer items.
REV - Reversal Items.

Contact your bank for the appropriate value.  */  
   "EntryClassCode":string,
      /**  The JrnlCode.JournalCode value of the Journal that will be used for A/P checks.  Normally this would be called Cash Disbursements Journal.  */  
   "CDJournalCode":string,
      /**  The JrnlCode.JournalCode value of the Journal that will be used for P/R checks.  Normally this would be called Payroll Journal.  */  
   "PRJournalCode":string,
      /**  The JrnlCode.JournalCode value of the Journal that will be used for A/R cash receipts. Normally this would be called the Cash Receipts Journal.  */  
   "CRJournalCode":string,
      /**  The JrnlCode.JournalCode value of the Journal that will be used for Bank transactions made in the check reconciliation process.  */  
   "BKJournalCode":string,
      /**  The identifier of the Bank Slip document (bank statement.) The user enters a bank slip during the bank reconciliation process.  This is then written into the related GLJrnDtl records. Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  */  
   "BankSlip":string,
      /**  Indicates if the decimal point in decimal fields should be exported when exporting electronic payments. For example, if this is set to no then 10.00 it would be exported as 1000.  */  
   "ExportDecimalPoint":boolean,
      /**  Currency.CurrencyCode of the currency that the bank account is denominated in.  */  
   "CurrencyCode":string,
      /**  Assigned by the bank.  Uniquely identifies your company to the bank.  */  
   "BankCompID":string,
      /**  Indicates whether or not the bank account is for Debit Notes only.  If this flag is yes the bank could be used in Cash Receipts  only.  */  
   "DebNoteOnly":boolean,
      /**  Allows you to keep a reconciled balance in AR when this check box is  */  
   "ReconciledBalance":boolean,
      /**  Allows you to keep a reconciled balance in AP when this check box is  */  
   "UsePendAcct":boolean,
      /**  Swift Number or ABA Routing Number  */  
   "BankIdentifier":string,
      /**  Bank Branch Code  */  
   "BankBranchCode":string,
      /**  IBAN Code  */  
   "IBANCode":string,
      /**  Use the bank average value as the rate for payments from this account.  */  
   "APPaymentUseBankAvg":boolean,
      /**  Payer Reference  */  
   "PayerRef":string,
      /**  Tax Payer ID  */  
   "TaxPayerID":string,
      /**  Future Use - Starting Number for Bank level PI Numbering  */  
   "NextPINum":number,
      /**  Tax Payer Registration Reason Code  */  
   "TaxRegReason":string,
      /**  Future Use - Number of digits allowed in PI Numbering  */  
   "NumPIDigits":number,
      /**  Correspondence Account  */  
   "CorrespAccount":string,
      /**  Local BIC  */  
   "LocalBIC":string,
      /**  Free Form Type Code. Used in localizations.  */  
   "TypeCode":string,
      /**  Free Form Person Name. Used in localizations.  */  
   "TransferPersonName":string,
      /**  Free Form Person code. Used in localizations.  */  
   "TransferPersonCode":string,
      /**  Account Type.  */  
   "AccountType":string,
      /**  Letter of Credit Limit.  */  
   "LOCLimit":number,
      /**  Legal Name of Bank, which is consistent with Legal Names field for trading partners.  */  
   "LegalName":string,
      /**  Float amount for the bank account.  */  
   "FloatAmt":number,
      /**  Letter of Credit Limit in bank's currency.  */  
   "DocLOCLimit":number,
      /**  Letter of Credit Limit in reporting currency 1.  */  
   "Rpt1LOCLimit":number,
      /**  Letter of Credit Limit in reporting currency 2.  */  
   "Rpt2LOCLimit":number,
      /**  Letter of Credit Limit in reporting currency 3.  */  
   "Rpt3LOCLimit":number,
      /**  Auto Statement Import  */  
   "AutoStatementImport":boolean,
      /**  Specifies whether the application automatically attempts to extract invoice numbers from the statement lines  */  
   "AutoMatchStatement":boolean,
      /**  Auto Rec Documents  */  
   "AutoRecDocuments":boolean,
      /**  Specifies a default electronic interface for importing bank statements for  */  
   "EFTHeadUID":number,
      /**  If this check box is selected, then after importing a bank statement the application automatically displays all  */  
   "AutoRetrieve":boolean,
      /**  Filter By Line  */  
   "FilterByLine":boolean,
      /**  CreditorID  */  
   "CreditorID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Specify whether reference number verification is applied during automatic  */  
   "AutoRcgARRefNum":boolean,
      /**  Specify whether customer verification is applied during automatic  */  
   "AutoRcgARCustomer":boolean,
      /**  Specify whether transaction date verification is applied during automatic  */  
   "AutoRcgARTranDate":boolean,
      /**  Specify whether reference number verification is applied during automatic  */  
   "AutoRcgAPRefNum":boolean,
      /**  Specify whether supplier verification is applied during automatic  */  
   "AutoRcgAPSupplier":boolean,
      /**  Specify whether transaction date verification is applied during automatic  */  
   "AutoRcgAPTranDate":boolean,
      /**  This parameter defines the application behavior in case the transactions do  */  
   "AutoRcgUnknownTran":boolean,
      /**  CHDTAID  */  
   "CHDTAID":string,
      /**  CHISRPartyID  */  
   "CHISRPartyID":string,
      /**  BankType  */  
   "BankType":string,
      /**  Select this checkbox to enable the automatic creation of invoice cash receipts.  */  
   "AutoCashMovement":boolean,
      /**  Specify the parsing parameter ID which is used during automatic bank  */  
   "ParamCode":string,
      /**  This check box determines the application logic when it cannot find invoices where customer, amount and date  */  
   "AutoOnAccountReceipt":boolean,
      /**  Auto Invoice Payment  */  
   "AutoInvoicePayment":boolean,
      /**  Select this checkbox to enable the automatic creation of same currency bank transfer transactions during automatic  */  
   "AutoBankTransferSameCurr":boolean,
      /**  Select this checkbox to enable the automatic creation of cross currency bank transfer transactions during automatic  */  
   "AutoBankTransferCrossCurr":boolean,
      /**  Select this checkbox to enable the automatic creation of bank adjustment transactions during automatic bank  */  
   "AutoBankAdjustment":boolean,
      /**  POBankAcctNum  */  
   "POBankAcctNum":string,
      /**  BankCustNum  */  
   "BankCustNum":string,
      /**  Select this check box to enable the automatic creation of reverse cash receipts and voided AP payments transactions  */  
   "AutoReverse":boolean,
      /**  Specifies the number of periods before opening date which will be retrieved during bank reconciliation. If you  */  
   "PeriodThreshold":number,
      /**  PRAlignTax  */  
   "PRAlignTax":boolean,
      /**  PRLinePerPRCheck  */  
   "PRLinePerPRCheck":number,
      /**  PRPreprintedCheckNumber  */  
   "PRPreprintedCheckNumber":boolean,
      /**  If you select this check box, the application sets the type of lines with  */  
   "PayrollCheckingAccount":boolean,
      /**  RBankNum  */  
   "RBankNum":string,
      /**  RBranchNum  */  
   "RBranchNum":string,
      /**  JPBankName  */  
   "JPBankName":string,
      /**  JPBranchName  */  
   "JPBranchName":string,
      /**  BankTranfAccountType  */  
   "BankTranfAccountType":string,
      /**  Address1  */  
   "Address1":string,
      /**  Address2  */  
   "Address2":string,
      /**  Address3  */  
   "Address3":string,
      /**  City  */  
   "City":string,
      /**  PostalCode  */  
   "PostalCode":string,
      /**  State  */  
   "State":string,
      /**  CountryNum  */  
   "CountryNum":number,
      /**  LName  */  
   "LName":string,
      /**  MsgIDCounter  */  
   "MsgIDCounter":string,
      /**  ConsInvPmt  */  
   "ConsInvPmt":boolean,
      /**  PreprintedCheckNum  */  
   "PreprintedCheckNum":boolean,
      /**  InvPerCheckStub  */  
   "InvPerCheckStub":number,
      /**  Allows you to keep a reconciled balance for transactions other than AP payments and AR cash receipts (such as  */  
   "ReconcileOtherBalances":boolean,
      /**  RecBalFiscalYear  */  
   "RecBalFiscalYear":number,
      /**  RecBalFiscalPeriod  */  
   "RecBalFiscalPeriod":number,
      /**  RecBalFiscalYearSuffix  */  
   "RecBalFiscalYearSuffix":string,
      /**  RevalueUseRecBal  */  
   "RevalueUseRecBal":boolean,
      /**  COOneTimeID  */  
   "COOneTimeID":string,
      /**  COIsOneTimeBankAcct  */  
   "COIsOneTimeBankAcct":boolean,
      /**  Select this checkbox to enable the automatic creation of cash receipts based on customer balance. This option  */  
   "AutoCustBalanceReceipt":boolean,
      /**  This parameter determines maximum allowed percent difference between amounts of the unallocated statement  */  
   "MatchTolerance":number,
      /**  Specify the ID of template with the set of transaction codes. It is assigned to the bank account. Refer to the Bank  */  
   "TranTemplateID":string,
      /**  This check box changes the application logic when it creates cash receipts based on customer balance.  */  
   "AutoCustBalanceReceiptApplyAll":boolean,
      /**  MXSATCode  */  
   "MXSATCode":string,
      /**  MXSATNameShort  */  
   "MXSATNameShort":string,
      /**  MXSATNameFull  */  
   "MXSATNameFull":string,
      /**  CNSellerBankName  */  
   "CNSellerBankName":string,
      /**  CNSellerAddress  */  
   "CNSellerAddress":string,
      /**  ClearBankExchRate  */  
   "ClearBankExchRate":string,
      /**  PositivePayRemoteID  */  
   "PositivePayRemoteID":string,
      /**  PositivePayBatchID  */  
   "PositivePayBatchID":string,
      /**  DefPosPayEFTHeadUID  */  
   "DefPosPayEFTHeadUID":number,
      /**  Font used when printing the logo in MICR check.  */  
   "LogoFont":string,
      /**  Logo type, stores "I" when is Image and "T" when is text and "Override in Blank" when the bank check doesn't need modifications.  */  
   "LogoType":string,
      /**  Image ID for the image used as logo in MICR check.  */  
   "LogoImageID":string,
      /**  First line for logo's text.  */  
   "LogoText01":string,
      /**  Second line for logo's text.  */  
   "LogoText02":string,
      /**  Third line for logo's text.  */  
   "LogoText03":string,
      /**  Fourth line for logo's text.  */  
   "LogoText04":string,
      /**  Fifth line for logo's text.  */  
   "LogoText05":string,
      /**  Sixth line for logo's text.  */  
   "LogoText06":string,
      /**  Font used when printing the signature in MICR check.  */  
   "SignatureFont":string,
      /**  Signature type, stores "I" when is Image and "T" when is text and "Override in Blank" when the bank check doesn't need modifications.  */  
   "SignatureType":string,
      /**  Image ID for the image used as signature in MICR check.  */  
   "SignatureImageID":string,
      /**  First line for signature's text.  */  
   "SignatureText01":string,
      /**  Second line for signature's text.  */  
   "SignatureText02":string,
      /**  Third line for signature's text.  */  
   "SignatureText03":string,
      /**  Fourth line for signature's text.  */  
   "SignatureText04":string,
      /**  Fifth line for signature's text.  */  
   "SignatureText05":string,
      /**  Sixth line for signature's text.  */  
   "SignatureText06":string,
      /**  To be used when processing the electronic interface for direct deposit check deductions.  */  
   "PREntryClassCode":string,
      /**  Id of the Electronic Interface to be used when processing a Payroll Group.  */  
   "PRPMEFTHeadUID":number,
      /**  PEDetNationalBank  */  
   "PEDetNationalBank":boolean,
      /**  BankGiroAcctNbr  */  
   "BankGiroAcctNbr":string,
      /**  Default Parent Site. This site is a default site that is paying for invoices.  */  
   "ParentPlant":string,
      /**  Default Child Sites. This is a default list of sites, which can be child sites at the time of payment  */  
   "ChildPlantList":string,
      /**  This option is to select which balances will be displayed (ongoing, reconciled, or non Reconciled).  */  
   "BalanceType":number,
   "BaseCurrCurrDesc":string,
   "BaseCurrCurrencyCode":string,
   "BaseCurrCurrencyID":string,
   "BaseCurrCurrName":string,
   "BaseCurrCurrSymbol":string,
   "BaseCurrDocumentDesc":string,
      /**  ISR Party Number in format XX-#####V-P (CSF Switzerland)  */  
   "CHScrISRPartyID":string,
   "CurrencySwitch":boolean,
      /**  Pay Method Type for Denmark localization  */  
   "PayMethod":string,
      /**  Pending Cash Account Description  */  
   "PendingCashAcctDesc":string,
      /**  Purchase and Expenditure Rate Group  */  
   "PORateGrp":string,
      /**  PO RateGrp Description  */  
   "PORateGrpDescription":string,
      /**  Variance Account Description  */  
   "VarianceAcctDesc":string,
      /**  This external field is created to hold the validation for the bank to be associated for any document. this will help to enable/disable field in case a crated bank account is already associated to any document or transaction.  */  
   "AssociatedToDoc":boolean,
      /**  Enable MICR Check panel  */  
   "EnableMICR":boolean,
   "BitFlag":number,
   "BankBranchCodeDescBankBranchCode":string,
   "BankBranchCodeDescDescription":string,
   "BKJournalCodeDescJrnlDescription":string,
   "CDJournalCodeDescJrnlDescription":string,
   "CRJournalCodeDescJrnlDescription":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrencyID":string,
   "DefPosPayEFTHeadUIDName":string,
   "EFTHeadName":string,
   "PRJournalCodeDescJrnlDescription":string,
   "PRPMEFTHeadUIDName":string,
   "XbSystSiteIsLegalEntity":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_BankPayMethodRow{
      /**  Company  */  
   "Company":string,
      /**  Unique identifier of the bank account  */  
   "BankAcctID":string,
      /**  Unique identifier of the payment method  */  
   "PMUID":number,
      /**  Flag for default payment method  */  
   "IsDefault":boolean,
      /**   Indicated the source of payment method
0 = AP payment method
1 = AR payment method  */  
   "PMSource":number,
      /**  PaymentNumMask  */  
   "PaymentNumMask":string,
      /**  StartingSeqNum  */  
   "StartingSeqNum":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  System row ID - GUID  */  
   "SysRowID":string,
      /**  This field will allow us to delete record marked as default.  */  
   "DeleteFromParent":boolean,
   "BitFlag":number,
   "PayMethodType":number,
   "PayMethodName":string,
   "PayMethodSummarizePerCustomer":boolean,
      /**  RowMod  */  
   "RowMod":string,
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
      @param proposedBankBranchCode
      @param ds
   */  
export interface ChangeBankBranchCode_input{
      /**  The proposed Bank Branch code  */  
   proposedBankBranchCode:string,
   ds:Erp_Tablesets_BankAcctTableset[],
}

export interface ChangeBankBranchCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankAcctTableset[],
}
}

   /** Required : 
      @param ds
      @param debNoteOnly
   */  
export interface ChangeDebNoteOnly_input{
   ds:Erp_Tablesets_BankAcctTableset[],
      /**  Proposed value of the flag  */  
   debNoteOnly:boolean,
}

export interface ChangeDebNoteOnly_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankAcctTableset[],
}
}

   /** Required : 
      @param proposedLOCLimit
      @param ds
   */  
export interface ChangeLOCLimit_input{
      /**  The proposed Limit amount  */  
   proposedLOCLimit:number,
   ds:Erp_Tablesets_BankAcctTableset[],
}

export interface ChangeLOCLimit_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankAcctTableset[],
}
}

   /** Required : 
      @param ipBankCustNum
   */  
export interface CheckBankCustNum_input{
      /**  New value of Bank Customer Number.  */  
   ipBankCustNum:string,
}

export interface CheckBankCustNum_output{
}

   /** Required : 
      @param ipISRPartyID
      @param ds
   */  
export interface CheckISRPartyID_input{
      /**  New value of ISR Party ID.  */  
   ipISRPartyID:string,
   ds:Erp_Tablesets_BankAcctTableset[],
}

export interface CheckISRPartyID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankAcctTableset[],
}
}

   /** Required : 
      @param bankAcctID
   */  
export interface DeleteByID_input{
   bankAcctID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_APLOCClosedRow{
      /**  Vendor Name  */  
   VendorName:string,
      /**  Vendor ID  */  
   VendorID:string,
      /**  Remaining Value  */  
   RemLCValue:number,
      /**  Outstanding PO Value  */  
   OutPOValue:number,
      /**  LC Value  */  
   LCValue:number,
      /**  Invoices Balance  */  
   InvoiceBal:number,
      /**  Letter of Credit Description  */  
   Description:string,
      /**  Currency Name  */  
   CurrName:string,
      /**  Cumulative Invoice Value  */  
   CumInvValue:number,
      /**  Letter of Credit ID.  */  
   APLCID:string,
   CurrencyCode:string,
      /**  Cumulative Invoice Value  */  
   DocCumInvValue:number,
      /**  Cumulative Invoice Value  */  
   Rpt1CumInvValue:number,
      /**  Cumulative Invoice Value  */  
   Rpt2CumInvValue:number,
      /**  Cumulative Invoice Value  */  
   Rpt3CumInvValue:number,
      /**  Invoices Balance  */  
   DocInvoiceBal:number,
      /**  Invoices Balance  */  
   Rpt1InvoiceBal:number,
      /**  Invoices Balance  */  
   Rpt2InvoiceBal:number,
      /**  Invoices Balance  */  
   Rpt3InvoiceBal:number,
      /**  Letter of Credit Value  */  
   DocLCValue:number,
      /**  Letter of Credit Value  */  
   Rpt1LCValue:number,
      /**  Letter of Credit Value  */  
   Rpt2LCValue:number,
      /**  Letter of Credit Value  */  
   Rpt3LCValue:number,
      /**  Outstanding PO Value  */  
   DocOutPOValue:number,
      /**  Outstanding PO Value  */  
   Rpt2OutPOValue:number,
      /**  Outstanding PO Value  */  
   Rpt3OutPOValue:number,
      /**  Remaining Value  */  
   DocRemLCValue:number,
      /**  Remaining Value  */  
   Rpt1RemLCValue:number,
      /**  Remaining Value  */  
   Rpt2RemLCValue:number,
      /**  Remaining Value  */  
   Rpt3RemLCValue:number,
      /**  Outstanding PO Value  */  
   Rpt1OutPOValue:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APLOCOpenRow{
      /**  Vendor Name  */  
   VendorName:string,
      /**  Letter of Credit ID  */  
   APLCID:string,
      /**  Cumulative Invoice Value  */  
   CumInvValue:number,
      /**  Currency Name  */  
   CurrName:string,
      /**  Letter of Credit Description  */  
   Description:string,
      /**  Invoices Balance  */  
   InvoiceBal:number,
      /**  LC Value  */  
   LCValue:number,
      /**  Outstanding PO Value  */  
   OutPOValue:number,
      /**  Remaining Value  */  
   RemLCValue:number,
      /**  Vendor ID  */  
   VendorID:string,
      /**  Cumulative Invoice Value  */  
   DocCumInvValue:number,
      /**  Cumulative Invoice Value  */  
   Rpt1CumInvValue:number,
      /**  Cumulative Invoice Value  */  
   Rpt2CumInvValue:number,
      /**  Cumulative Invoice Value  */  
   Rpt3CumInvValue:number,
      /**  Invoices Balance  */  
   DocInvoiceBal:number,
      /**  Invoices Balance  */  
   Rpt1InvoiceBal:number,
      /**  Invoices Balance  */  
   Rpt2InvoiceBal:number,
      /**  Invoices Balance  */  
   Rpt3InvoiceBal:number,
      /**  Letter of Credit Value  */  
   DocLCValue:number,
      /**  Letter of Credit Value  */  
   Rpt1LCValue:number,
      /**  Letter of Credit Value  */  
   Rpt2LCValue:number,
      /**  Letter of Credit Value  */  
   Rpt3LCValue:number,
      /**  Outstanding PO Value  */  
   DocOutPOValue:number,
      /**  Outstanding PO Value  */  
   Rpt1OutPOValue:number,
      /**  Outstanding PO Value  */  
   Rpt2OutPOValue:number,
      /**  Outstanding PO Value  */  
   Rpt3OutPOValue:number,
      /**  Remaining Value  */  
   DocRemLCValue:number,
      /**  Remaining Value  */  
   Rpt1RemLCValue:number,
      /**  Remaining Value  */  
   Rpt2RemLCValue:number,
      /**  Remaining Value  */  
   Rpt3RemLCValue:number,
   CurrencyCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BalanceRow{
   Company:string,
   BankAcctID:string,
      /**  Enter the fiscal year whose balances you want to display. By default, the current fiscal year is selected.  */  
   FiscalYear:number,
   FiscalPeriod:number,
   CurrencyCode:string,
   ExchangeRate:number,
   RefToBaseRate:number,
   RefCode:string,
   DocToRef:boolean,
   RefToBase:boolean,
   DbBalance:number,
   CrBalance:number,
   OpeningBalance:number,
   DocDbBalance:number,
   DocCrBalance:number,
   DocOpeningBalance:number,
      /**  The current balance total  */  
   CurrentBalance:number,
      /**  The document current balance total.  */  
   DocCurrentBalance:number,
      /**  The currency switch flag  */  
   CurrencySwitch:boolean,
      /**  The currency symbol.  */  
   CurrSymbol:string,
      /**  Base Currency Symbol based on the current Company  */  
   BaseCurrencySymbol:string,
      /**  Enter the fiscal year suffix whose balances you want to display.  */  
   FiscalYearSuffix:string,
   FiscalCalendarID:string,
   Rpt1CrBalance:number,
   Rpt2CrBalance:number,
   Rpt3CrBalance:number,
   Rpt1DbBalance:number,
   Rpt2DbBalance:number,
   Rpt3DbBalance:number,
   Rpt1OpeningBalance:number,
   Rpt2OpeningBalance:number,
   Rpt3OpeningBalance:number,
   Rpt1CurrentBalance:number,
   Rpt2CurrentBalance:number,
   Rpt3CurrentBalance:number,
   OpeningBalanceRec:number,
   CrBalanceRec:number,
   DbBalanceRec:number,
   CurrentBalanceRec:number,
   DocOpeningBalanceRec:number,
   DocCrBalanceRec:number,
   DocDbBalanceRec:number,
   DocCurrentBalanceRec:number,
   Rpt1OpeningBalanceRec:number,
   Rpt1CrBalanceRec:number,
   Rpt1DbBalanceRec:number,
   Rpt1CurrentBalanceRec:number,
   Rpt2OpeningBalanceRec:number,
   Rpt2CrBalanceRec:number,
   Rpt2DbBalanceRec:number,
   Rpt2CurrentBalanceRec:number,
   Rpt3OpeningBalanceRec:number,
   Rpt3CrBalanceRec:number,
   Rpt3DbBalanceRec:number,
   Rpt3CurrentBalanceRec:number,
   OpeningBalanceNonRec:number,
   CrBalanceNonRec:number,
   DbBalanceNonRec:number,
   CurrentBalanceNonRec:number,
   DocOpeningBalanceNonRec:number,
   DocCrBalanceNonRec:number,
   DocDbBalanceNonRec:number,
   DocCurrentBalanceNonRec:number,
   Rpt1OpeningBalanceNonRec:number,
   Rpt1CrBalanceNonRec:number,
   Rpt1DbBalanceNonRec:number,
   Rpt1CurrentBalanceNonRec:number,
   Rpt2OpeningBalanceNonRec:number,
   Rpt2CrBalanceNonRec:number,
   Rpt2DbBalanceNonRec:number,
   Rpt2CurrentBalanceNonRec:number,
   Rpt3OpeningBalanceNonRec:number,
   Rpt3CrBalanceNonRec:number,
   Rpt3DbBalanceNonRec:number,
   Rpt3CurrentBalanceNonRec:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BalanceTableset{
   Balance:Erp_Tablesets_BalanceRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_BankAcctAttchRow{
   Company:string,
   BankAcctID:string,
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

export interface Erp_Tablesets_BankAcctListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of the bank account assigned by the user.  */  
   BankAcctID:string,
      /**  Full description of the bank account.  */  
   Description:string,
      /**  The account number for the bank account. Used for reference only.  */  
   CheckingAccount:string,
      /**  Indicates whether or not the bank account is an active account.  */  
   Closed:boolean,
      /**  Swift Number or ABA Routing Number  */  
   BankIdentifier:string,
      /**  IBAN Code  */  
   IBANCode:string,
      /**  Use the bank average value as the rate for payments from this account.  */  
   APPaymentUseBankAvg:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates of bank account that now have an open statement waiting to be finally matched/posted.  */  
   OpenStatement:boolean,
      /**  PositivePayRemoteID  */  
   PositivePayRemoteID:string,
      /**  PositivePayBatchID  */  
   PositivePayBatchID:string,
      /**  DefPosPayEFTHeadUID  */  
   DefPosPayEFTHeadUID:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BankAcctListTableset{
   BankAcctList:Erp_Tablesets_BankAcctListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_BankAcctRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of the bank account assigned by the user.  */  
   BankAcctID:string,
      /**  Full description of the bank account.  */  
   Description:string,
      /**  The account number for the bank account. Used for reference only.  */  
   CheckingAccount:string,
      /**  Indicates whether or not the bank account is an active account.  */  
   Closed:boolean,
      /**  The Opening Balance of the Bank Account. When a bank reconciliation is posted, this field is set to the posted reconciliation's closing balance and becomes the opening balance for the next statement.  */  
   OpeningBalance:number,
      /**  The Opening Date of the Bank Account.  When a bank reconciliation is posted, the next statement's opening date is set to the posted reconciliation's Closing Date + 1 and becomes the opening date for the next statement.  */  
   OpeningDate:string,
      /**  The Closing Balance of the Bank Account. When a bank reconciliation is posted, this field is set to the posted reconciliation's closing balance.  */  
   ClosingBalance:number,
      /**  The Closing Date of the Bank Account. When a bank reconciliation is posted, this field is set to the posted reconciliation's closing date.  */  
   ClosingDate:string,
      /**  The bank's routing number.  */  
   BankRoutingNum:string,
      /**  The check digit for the bank.  */  
   BankCheckDigit:number,
      /**  The Bank's full name.  */  
   BankName:string,
      /**   Service Class Code 200 = Mixed debit or credit entries and pre-notification entries.

Contact your bank for the appropriate value.  */  
   ServClassCode:string,
      /**   PPD - Prearranged Payments and Deposits for consumer items.
CCD - Cash concentration and disbursements for non-consumer items.
REV - Reversal Items.

Contact your bank for the appropriate value.  */  
   EntryClassCode:string,
      /**  The JrnlCode.JournalCode value of the Journal that will be used for A/P checks.  Normally this would be called Cash Disbursements Journal.  */  
   CDJournalCode:string,
      /**  The JrnlCode.JournalCode value of the Journal that will be used for P/R checks.  Normally this would be called Payroll Journal.  */  
   PRJournalCode:string,
      /**  The JrnlCode.JournalCode value of the Journal that will be used for A/R cash receipts. Normally this would be called the Cash Receipts Journal.  */  
   CRJournalCode:string,
      /**  The JrnlCode.JournalCode value of the Journal that will be used for Bank transactions made in the check reconciliation process.  */  
   BKJournalCode:string,
      /**  The identifier of the Bank Slip document (bank statement.) The user enters a bank slip during the bank reconciliation process.  This is then written into the related GLJrnDtl records. Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  */  
   BankSlip:string,
      /**  Indicates if the decimal point in decimal fields should be exported when exporting electronic payments. For example, if this is set to no then 10.00 it would be exported as 1000.  */  
   ExportDecimalPoint:boolean,
      /**  Currency.CurrencyCode of the currency that the bank account is denominated in.  */  
   CurrencyCode:string,
      /**  Assigned by the bank.  Uniquely identifies your company to the bank.  */  
   BankCompID:string,
      /**  Indicates whether or not the bank account is for Debit Notes only.  If this flag is yes the bank could be used in Cash Receipts  only.  */  
   DebNoteOnly:boolean,
      /**  Allows you to keep a reconciled balance in AR when this check box is  */  
   ReconciledBalance:boolean,
      /**  Allows you to keep a reconciled balance in AP when this check box is  */  
   UsePendAcct:boolean,
      /**  Swift Number or ABA Routing Number  */  
   BankIdentifier:string,
      /**  Bank Branch Code  */  
   BankBranchCode:string,
      /**  IBAN Code  */  
   IBANCode:string,
      /**  Use the bank average value as the rate for payments from this account.  */  
   APPaymentUseBankAvg:boolean,
      /**  Payer Reference  */  
   PayerRef:string,
      /**  Tax Payer ID  */  
   TaxPayerID:string,
      /**  Future Use - Starting Number for Bank level PI Numbering  */  
   NextPINum:number,
      /**  Tax Payer Registration Reason Code  */  
   TaxRegReason:string,
      /**  Future Use - Number of digits allowed in PI Numbering  */  
   NumPIDigits:number,
      /**  Correspondence Account  */  
   CorrespAccount:string,
      /**  Local BIC  */  
   LocalBIC:string,
      /**  Free Form Type Code. Used in localizations.  */  
   TypeCode:string,
      /**  Free Form Person Name. Used in localizations.  */  
   TransferPersonName:string,
      /**  Free Form Person code. Used in localizations.  */  
   TransferPersonCode:string,
      /**  Account Type.  */  
   AccountType:string,
      /**  Letter of Credit Limit.  */  
   LOCLimit:number,
      /**  Legal Name of Bank, which is consistent with Legal Names field for trading partners.  */  
   LegalName:string,
      /**  Float amount for the bank account.  */  
   FloatAmt:number,
      /**  Letter of Credit Limit in bank's currency.  */  
   DocLOCLimit:number,
      /**  Letter of Credit Limit in reporting currency 1.  */  
   Rpt1LOCLimit:number,
      /**  Letter of Credit Limit in reporting currency 2.  */  
   Rpt2LOCLimit:number,
      /**  Letter of Credit Limit in reporting currency 3.  */  
   Rpt3LOCLimit:number,
      /**  Auto Statement Import  */  
   AutoStatementImport:boolean,
      /**  Specifies whether the application automatically attempts to extract invoice numbers from the statement lines  */  
   AutoMatchStatement:boolean,
      /**  Auto Rec Documents  */  
   AutoRecDocuments:boolean,
      /**  Specifies a default electronic interface for importing bank statements for  */  
   EFTHeadUID:number,
      /**  If this check box is selected, then after importing a bank statement the application automatically displays all  */  
   AutoRetrieve:boolean,
      /**  Filter By Line  */  
   FilterByLine:boolean,
      /**  CreditorID  */  
   CreditorID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Specify whether reference number verification is applied during automatic  */  
   AutoRcgARRefNum:boolean,
      /**  Specify whether customer verification is applied during automatic  */  
   AutoRcgARCustomer:boolean,
      /**  Specify whether transaction date verification is applied during automatic  */  
   AutoRcgARTranDate:boolean,
      /**  Specify whether reference number verification is applied during automatic  */  
   AutoRcgAPRefNum:boolean,
      /**  Specify whether supplier verification is applied during automatic  */  
   AutoRcgAPSupplier:boolean,
      /**  Specify whether transaction date verification is applied during automatic  */  
   AutoRcgAPTranDate:boolean,
      /**  This parameter defines the application behavior in case the transactions do  */  
   AutoRcgUnknownTran:boolean,
      /**  CHDTAID  */  
   CHDTAID:string,
      /**  CHISRPartyID  */  
   CHISRPartyID:string,
      /**  BankType  */  
   BankType:string,
      /**  Select this checkbox to enable the automatic creation of invoice cash receipts.  */  
   AutoCashMovement:boolean,
      /**  Specify the parsing parameter ID which is used during automatic bank  */  
   ParamCode:string,
      /**  This check box determines the application logic when it cannot find invoices where customer, amount and date  */  
   AutoOnAccountReceipt:boolean,
      /**  Auto Invoice Payment  */  
   AutoInvoicePayment:boolean,
      /**  Select this checkbox to enable the automatic creation of same currency bank transfer transactions during automatic  */  
   AutoBankTransferSameCurr:boolean,
      /**  Select this checkbox to enable the automatic creation of cross currency bank transfer transactions during automatic  */  
   AutoBankTransferCrossCurr:boolean,
      /**  Select this checkbox to enable the automatic creation of bank adjustment transactions during automatic bank  */  
   AutoBankAdjustment:boolean,
      /**  POBankAcctNum  */  
   POBankAcctNum:string,
      /**  BankCustNum  */  
   BankCustNum:string,
      /**  Select this check box to enable the automatic creation of reverse cash receipts and voided AP payments transactions  */  
   AutoReverse:boolean,
      /**  Specifies the number of periods before opening date which will be retrieved during bank reconciliation. If you  */  
   PeriodThreshold:number,
      /**  PRAlignTax  */  
   PRAlignTax:boolean,
      /**  PRLinePerPRCheck  */  
   PRLinePerPRCheck:number,
      /**  PRPreprintedCheckNumber  */  
   PRPreprintedCheckNumber:boolean,
      /**  If you select this check box, the application sets the type of lines with  */  
   PayrollCheckingAccount:boolean,
      /**  RBankNum  */  
   RBankNum:string,
      /**  RBranchNum  */  
   RBranchNum:string,
      /**  JPBankName  */  
   JPBankName:string,
      /**  JPBranchName  */  
   JPBranchName:string,
      /**  BankTranfAccountType  */  
   BankTranfAccountType:string,
      /**  Address1  */  
   Address1:string,
      /**  Address2  */  
   Address2:string,
      /**  Address3  */  
   Address3:string,
      /**  City  */  
   City:string,
      /**  PostalCode  */  
   PostalCode:string,
      /**  State  */  
   State:string,
      /**  CountryNum  */  
   CountryNum:number,
      /**  LName  */  
   LName:string,
      /**  MsgIDCounter  */  
   MsgIDCounter:string,
      /**  ConsInvPmt  */  
   ConsInvPmt:boolean,
      /**  PreprintedCheckNum  */  
   PreprintedCheckNum:boolean,
      /**  InvPerCheckStub  */  
   InvPerCheckStub:number,
      /**  Allows you to keep a reconciled balance for transactions other than AP payments and AR cash receipts (such as  */  
   ReconcileOtherBalances:boolean,
      /**  RecBalFiscalYear  */  
   RecBalFiscalYear:number,
      /**  RecBalFiscalPeriod  */  
   RecBalFiscalPeriod:number,
      /**  RecBalFiscalYearSuffix  */  
   RecBalFiscalYearSuffix:string,
      /**  RevalueUseRecBal  */  
   RevalueUseRecBal:boolean,
      /**  COOneTimeID  */  
   COOneTimeID:string,
      /**  COIsOneTimeBankAcct  */  
   COIsOneTimeBankAcct:boolean,
      /**  Select this checkbox to enable the automatic creation of cash receipts based on customer balance. This option  */  
   AutoCustBalanceReceipt:boolean,
      /**  This parameter determines maximum allowed percent difference between amounts of the unallocated statement  */  
   MatchTolerance:number,
      /**  Specify the ID of template with the set of transaction codes. It is assigned to the bank account. Refer to the Bank  */  
   TranTemplateID:string,
      /**  This check box changes the application logic when it creates cash receipts based on customer balance.  */  
   AutoCustBalanceReceiptApplyAll:boolean,
      /**  MXSATCode  */  
   MXSATCode:string,
      /**  MXSATNameShort  */  
   MXSATNameShort:string,
      /**  MXSATNameFull  */  
   MXSATNameFull:string,
      /**  CNSellerBankName  */  
   CNSellerBankName:string,
      /**  CNSellerAddress  */  
   CNSellerAddress:string,
      /**  ClearBankExchRate  */  
   ClearBankExchRate:string,
      /**  PositivePayRemoteID  */  
   PositivePayRemoteID:string,
      /**  PositivePayBatchID  */  
   PositivePayBatchID:string,
      /**  DefPosPayEFTHeadUID  */  
   DefPosPayEFTHeadUID:number,
      /**  Font used when printing the logo in MICR check.  */  
   LogoFont:string,
      /**  Logo type, stores "I" when is Image and "T" when is text and "Override in Blank" when the bank check doesn't need modifications.  */  
   LogoType:string,
      /**  Image ID for the image used as logo in MICR check.  */  
   LogoImageID:string,
      /**  First line for logo's text.  */  
   LogoText01:string,
      /**  Second line for logo's text.  */  
   LogoText02:string,
      /**  Third line for logo's text.  */  
   LogoText03:string,
      /**  Fourth line for logo's text.  */  
   LogoText04:string,
      /**  Fifth line for logo's text.  */  
   LogoText05:string,
      /**  Sixth line for logo's text.  */  
   LogoText06:string,
      /**  Font used when printing the signature in MICR check.  */  
   SignatureFont:string,
      /**  Signature type, stores "I" when is Image and "T" when is text and "Override in Blank" when the bank check doesn't need modifications.  */  
   SignatureType:string,
      /**  Image ID for the image used as signature in MICR check.  */  
   SignatureImageID:string,
      /**  First line for signature's text.  */  
   SignatureText01:string,
      /**  Second line for signature's text.  */  
   SignatureText02:string,
      /**  Third line for signature's text.  */  
   SignatureText03:string,
      /**  Fourth line for signature's text.  */  
   SignatureText04:string,
      /**  Fifth line for signature's text.  */  
   SignatureText05:string,
      /**  Sixth line for signature's text.  */  
   SignatureText06:string,
      /**  To be used when processing the electronic interface for direct deposit check deductions.  */  
   PREntryClassCode:string,
      /**  Id of the Electronic Interface to be used when processing a Payroll Group.  */  
   PRPMEFTHeadUID:number,
      /**  PEDetNationalBank  */  
   PEDetNationalBank:boolean,
      /**  BankGiroAcctNbr  */  
   BankGiroAcctNbr:string,
      /**  Default Parent Site. This site is a default site that is paying for invoices.  */  
   ParentPlant:string,
      /**  Default Child Sites. This is a default list of sites, which can be child sites at the time of payment  */  
   ChildPlantList:string,
      /**  This option is to select which balances will be displayed (ongoing, reconciled, or non Reconciled).  */  
   BalanceType:number,
   BaseCurrCurrDesc:string,
   BaseCurrCurrencyCode:string,
   BaseCurrCurrencyID:string,
   BaseCurrCurrName:string,
   BaseCurrCurrSymbol:string,
   BaseCurrDocumentDesc:string,
      /**  ISR Party Number in format XX-#####V-P (CSF Switzerland)  */  
   CHScrISRPartyID:string,
   CurrencySwitch:boolean,
      /**  Pay Method Type for Denmark localization  */  
   PayMethod:string,
      /**  Pending Cash Account Description  */  
   PendingCashAcctDesc:string,
      /**  Purchase and Expenditure Rate Group  */  
   PORateGrp:string,
      /**  PO RateGrp Description  */  
   PORateGrpDescription:string,
      /**  Variance Account Description  */  
   VarianceAcctDesc:string,
      /**  This external field is created to hold the validation for the bank to be associated for any document. this will help to enable/disable field in case a crated bank account is already associated to any document or transaction.  */  
   AssociatedToDoc:boolean,
      /**  Enable MICR Check panel  */  
   EnableMICR:boolean,
   BitFlag:number,
   BankBranchCodeDescBankBranchCode:string,
   BankBranchCodeDescDescription:string,
   BKJournalCodeDescJrnlDescription:string,
   CDJournalCodeDescJrnlDescription:string,
   CRJournalCodeDescJrnlDescription:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrencyID:string,
   DefPosPayEFTHeadUIDName:string,
   EFTHeadName:string,
   PRJournalCodeDescJrnlDescription:string,
   PRPMEFTHeadUIDName:string,
   XbSystSiteIsLegalEntity:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BankAcctTableset{
   BankAcct:Erp_Tablesets_BankAcctRow[],
   BankAcctAttch:Erp_Tablesets_BankAcctAttchRow[],
   BankPayMethod:Erp_Tablesets_BankPayMethodRow[],
   Partner:Erp_Tablesets_PartnerRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_BankAcctTrackerTableset{
   APLOCClosed:Erp_Tablesets_APLOCClosedRow[],
   APLOCOpen:Erp_Tablesets_APLOCOpenRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_BankPayMethodRow{
      /**  Company  */  
   Company:string,
      /**  Unique identifier of the bank account  */  
   BankAcctID:string,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  Flag for default payment method  */  
   IsDefault:boolean,
      /**   Indicated the source of payment method
0 = AP payment method
1 = AR payment method  */  
   PMSource:number,
      /**  PaymentNumMask  */  
   PaymentNumMask:string,
      /**  StartingSeqNum  */  
   StartingSeqNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  System row ID - GUID  */  
   SysRowID:string,
      /**  This field will allow us to delete record marked as default.  */  
   DeleteFromParent:boolean,
   BitFlag:number,
   PayMethodType:number,
   PayMethodName:string,
   PayMethodSummarizePerCustomer:boolean,
      /**  RowMod  */  
   RowMod:string,
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

export interface Erp_Tablesets_UpdExtBankAcctTableset{
   BankAcct:Erp_Tablesets_BankAcctRow[],
   BankAcctAttch:Erp_Tablesets_BankAcctAttchRow[],
   BankPayMethod:Erp_Tablesets_BankPayMethodRow[],
   Partner:Erp_Tablesets_PartnerRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param bankAcctID
   */  
export interface GetAPLOCClosed_input{
      /**  Bank Account ID  */  
   bankAcctID:string,
}

export interface GetAPLOCClosed_output{
   returnObj:Erp_Tablesets_BankAcctTrackerTableset[],
}

   /** Required : 
      @param bankAcctID
   */  
export interface GetAPLOCOpen_input{
      /**  Bank Account ID  */  
   bankAcctID:string,
}

export interface GetAPLOCOpen_output{
   returnObj:Erp_Tablesets_BankAcctTrackerTableset[],
}

   /** Required : 
      @param date
      @param bankID
   */  
export interface GetBankBalFromDate_input{
      /**  Date  */  
   date:string,
      /**  Bank ID  */  
   bankID:string,
}

export interface GetBankBalFromDate_output{
   returnObj:Erp_Tablesets_BalanceTableset[],
}

   /** Required : 
      @param fyear
      @param fyearsuffix
      @param bankID
   */  
export interface GetBankBal_input{
      /**  Fiscal Year  */  
   fyear:number,
      /**  Fiscal Year Suffix  */  
   fyearsuffix:string,
      /**  Bank ID  */  
   bankID:string,
}

export interface GetBankBal_output{
   returnObj:Erp_Tablesets_BalanceTableset[],
}

export interface GetBaseCurrencySymbol_output{
   returnObj:string,
}

   /** Required : 
      @param bankAcctID
   */  
export interface GetByID_input{
   bankAcctID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_BankAcctTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_BankAcctTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_BankAcctTableset[],
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

export interface GetCurrencyBase_output{
parameters : {
      /**  output parameters  */  
   opCurrencyBase:string,
}
}

   /** Required : 
      @param bankAcctID
   */  
export interface GetEnableMICR_input{
   bankAcctID:string,
}

export interface GetEnableMICR_output{
   returnObj:boolean,
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
   returnObj:Erp_Tablesets_BankAcctListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param bankAcctID
   */  
export interface GetNewBankAcctAttch_input{
   ds:Erp_Tablesets_BankAcctTableset[],
   bankAcctID:string,
}

export interface GetNewBankAcctAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankAcctTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewBankAcct_input{
   ds:Erp_Tablesets_BankAcctTableset[],
}

export interface GetNewBankAcct_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankAcctTableset[],
}
}

   /** Required : 
      @param ds
      @param bankAcctID
   */  
export interface GetNewBankPayMethod_input{
   ds:Erp_Tablesets_BankAcctTableset[],
   bankAcctID:string,
}

export interface GetNewBankPayMethod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankAcctTableset[],
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
   ds:Erp_Tablesets_BankAcctTableset[],
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
   ds:Erp_Tablesets_BankAcctTableset[],
}
}

   /** Required : 
      @param ds
      @param partnerNum
      @param partnerType
      @param partnerID
   */  
export interface GetNewPartner_input{
   ds:Erp_Tablesets_BankAcctTableset[],
   partnerNum:number,
   partnerType:number,
   partnerID:string,
}

export interface GetNewPartner_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankAcctTableset[],
}
}

   /** Required : 
      @param whereClauseBankAcct
      @param whereClauseBankAcctAttch
      @param whereClauseBankPayMethod
      @param whereClauseEntityGLC
      @param whereClausePartner
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForMandate_input{
      /**  Base Whereclause for BankAcct table.  */  
   whereClauseBankAcct:string,
      /**  Base Whereclause for BankAcctAttch.  */  
   whereClauseBankAcctAttch:string,
      /**  Whereclause for BankPayMethod table  */  
   whereClauseBankPayMethod:string,
      /**  Whereclause for EntityGLC table  */  
   whereClauseEntityGLC:string,
      /**  Whereclause for Partner table  */  
   whereClausePartner:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsForMandate_output{
   returnObj:Erp_Tablesets_BankAcctTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseBankAcct
      @param whereClauseBankAcctAttch
      @param whereClauseBankPayMethod
      @param whereClausePartner
      @param whereClauseEntityGLC
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseBankAcct:string,
   whereClauseBankAcctAttch:string,
   whereClauseBankPayMethod:string,
   whereClausePartner:string,
   whereClauseEntityGLC:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_BankAcctTableset[],
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
      @param ds
   */  
export interface ModifySearchIDs_input{
   ds:Erp_Tablesets_BankAcctTableset[],
}

export interface ModifySearchIDs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankAcctTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtBankAcctTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtBankAcctTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_BankAcctTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankAcctTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ValidatePartner_input{
   ds:Erp_Tablesets_BankAcctTableset[],
}

export interface ValidatePartner_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankAcctTableset[],
}
}

