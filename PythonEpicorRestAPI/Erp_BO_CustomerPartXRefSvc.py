import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CustomerPartXRefSvc
# Description: Customer Part Cross References BO
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CustomerPartXRefs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CustomerPartXRefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CustomerPartXRefs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustXPrtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/CustomerPartXRefs",headers=creds) as resp:
           return await resp.json()

async def post_CustomerPartXRefs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CustomerPartXRefs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CustXPrtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CustXPrtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/CustomerPartXRefs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CustomerPartXRefs_Company_CustNum_PartNum_XPartNum_SysRowID(Company, CustNum, PartNum, XPartNum, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CustomerPartXRef item
   Description: Calls GetByID to retrieve the CustomerPartXRef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustomerPartXRef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param XPartNum: Desc: XPartNum   Required: True   Allow empty value : True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CustXPrtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/CustomerPartXRefs(" + Company + "," + CustNum + "," + PartNum + "," + XPartNum + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CustomerPartXRefs_Company_CustNum_PartNum_XPartNum_SysRowID(Company, CustNum, PartNum, XPartNum, SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CustomerPartXRef for the service
   Description: Calls UpdateExt to update CustomerPartXRef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CustomerPartXRef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param XPartNum: Desc: XPartNum   Required: True   Allow empty value : True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CustXPrtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/CustomerPartXRefs(" + Company + "," + CustNum + "," + PartNum + "," + XPartNum + "," + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CustomerPartXRefs_Company_CustNum_PartNum_XPartNum_SysRowID(Company, CustNum, PartNum, XPartNum, SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CustomerPartXRef item
   Description: Call UpdateExt to delete CustomerPartXRef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CustomerPartXRef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param XPartNum: Desc: XPartNum   Required: True   Allow empty value : True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/CustomerPartXRefs(" + Company + "," + CustNum + "," + PartNum + "," + XPartNum + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustXPrtListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCustXPrt, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCustXPrt=" + whereClauseCustXPrt
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(custNum, partNum, xpartNum, sysRowID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "custNum=" + custNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "partNum=" + partNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "xpartNum=" + xpartNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "sysRowID=" + sysRowID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCustXPrtPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCustXPrtPartNum
   Description: When Changing CustXPrt.PartNum field.
   OperationID: ChangeCustXPrtPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCustXPrtPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustXPrtPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeListCustXPrtPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeListCustXPrtPartNum
   Description: When Changing CustXPrtList.PartNum field.
   OperationID: ChangeListCustXPrtPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeListCustXPrtPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeListCustXPrtPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCustXPrtSNMask(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCustXPrtSNMask
   Description: When Changing CustXPrt.SNMask field.
   OperationID: ChangeCustXPrtSNMask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCustXPrtSNMask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustXPrtSNMask_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCustXPrtSNOverride(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCustXPrtSNOverride
   Description: When Changing PartRef.SNOverride field.
   OperationID: ChangeCustXPrtSNOverride
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCustXPrtSNOverride_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustXPrtSNOverride_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCustXPrtXPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCustXPrtXPartNum
   Description: When Changing CustXPrt.XPartNum field.
   OperationID: ChangeCustXPrtXPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCustXPrtXPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustXPrtXPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsCustXPrtXPartNumInvalid(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsCustXPrtXPartNumInvalid
   Description: when Changing Customer Part Num
   OperationID: IsCustXPrtXPartNumInvalid
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsCustXPrtXPartNumInvalid_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsCustXPrtXPartNumInvalid_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMaskPrefixSuffix(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMaskPrefixSuffix
   Description: When Changing CustomerRef.MaskPrefix or Suffix field.
   OperationID: ChangeMaskPrefixSuffix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMaskPrefixSuffix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMaskPrefixSuffix_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCustomerParXRef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCustomerParXRef
   Description: Get all Customer Part References for a given Customer
   OperationID: GetCustomerParXRef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustomerParXRef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustomerParXRef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindCustPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindCustPartNum
   Description: Find Customer Part Number.
   OperationID: FindCustPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindCustPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindCustPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCustPartXCustPartRef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCustPartXCustPartRef
   Description: Get Customer Part Cross References for a given Customer and PartNum
   OperationID: GetCustPartXCustPartRef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustPartXCustPartRef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustPartXCustPartRef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListCustPartXCustPartRef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCustPartXCustPartRef
   Description: Get Customer Part Cross References List for a given Customer and PartNum
   OperationID: GetListCustPartXCustPartRef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustPartXCustPartRef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustPartXCustPartRef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListCustPartXCustPartRefByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCustPartXCustPartRefByID
   Description: Get Customer Part Cross References List for a List of GUIDs
   OperationID: GetListCustPartXCustPartRefByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustPartXCustPartRefByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustPartXCustPartRefByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateCustPartOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateCustPartOpts
   Description: Update Customer CustPartOpts
   OperationID: UpdateCustPartOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateCustPartOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCustPartOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByPart
   OperationID: DeleteByPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCustXPrt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCustXPrt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCustXPrt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCustXPrt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCustXPrt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustomerPartXRefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustXPrtListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CustXPrtListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustXPrtRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CustXPrtRow] = obj["value"]
      pass

class Erp_Tablesets_CustXPrtListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Our Part number used to identify this part.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number of this part cross reference record  """  
      self.XPartNum:str = obj["XPartNum"]
      """  Part Number that the customer uses to identify the Part.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Customers Part Revision Number.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Description Customer uses to describes the Part.  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNMaskExample:str = obj["SNMaskExample"]
      """  BL-generated example of the serial number mask if SNBaseDataType = Mask.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.SNOverride:bool = obj["SNOverride"]
      """  Override serial mask settings? SN fields are ignored unless this is true.  """  
      self.GlobalCustXPrt:bool = obj["GlobalCustXPrt"]
      """  Marks this CustXPrt as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.WIApplication:str = obj["WIApplication"]
      """  WIApplication  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EDIContainerType:str = obj["EDIContainerType"]
      """  EDIContainerType  """  
      self.ProductionPartNum:str = obj["ProductionPartNum"]
      """  ProductionPartNum  """  
      self.ProductionPartNumIsValid:bool = obj["ProductionPartNumIsValid"]
      """  ProductionPartNumIsValid  """  
      self.ServicePartNum:str = obj["ServicePartNum"]
      """  ServicePartNum  """  
      self.ServicePartNumIsValid:bool = obj["ServicePartNumIsValid"]
      """  ServicePartNumIsValid  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustXPrtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Our Part number used to identify this part.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number of this part cross reference record  """  
      self.XPartNum:str = obj["XPartNum"]
      """  Part Number that the customer uses to identify the Part.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Customers Part Revision Number.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Description Customer uses to describes the Part.  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNMaskExample:str = obj["SNMaskExample"]
      """  BL-generated example of the serial number mask if SNBaseDataType = Mask.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.SNOverride:bool = obj["SNOverride"]
      """  Override serial mask settings? SN fields are ignored unless this is true.  """  
      self.GlobalCustXPrt:bool = obj["GlobalCustXPrt"]
      """  Marks this CustXPrt as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.WIApplication:str = obj["WIApplication"]
      """  WIApplication  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EDIContainerType:str = obj["EDIContainerType"]
      """  EDIContainerType  """  
      self.ProductionPartNum:str = obj["ProductionPartNum"]
      """  ProductionPartNum  """  
      self.ProductionPartNumIsValid:bool = obj["ProductionPartNumIsValid"]
      """  ProductionPartNumIsValid  """  
      self.ServicePartNum:str = obj["ServicePartNum"]
      """  ServicePartNum  """  
      self.ServicePartNumIsValid:bool = obj["ServicePartNumIsValid"]
      """  ServicePartNumIsValid  """  
      self.SNPrefixExampleSuffix:str = obj["SNPrefixExampleSuffix"]
      """  Prefix + Example + Suffix  """  
      self.SuffixLength:int = obj["SuffixLength"]
      """  SuffixLength  """  
      self.PrefixLength:int = obj["PrefixLength"]
      """  PrefixLength  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeCustXPrtPartNum_input:
   """ Required : 
   iPartNum
   ds
   sysRowID
   rowType
   """  
   def __init__(self, obj):
      self.iPartNum:str = obj["iPartNum"]
      """  Part Number  """  
      self.ds:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["ds"]
      self.sysRowID:str = obj["sysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      pass

class ChangeCustXPrtPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.iPartNum:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["ds"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class ChangeCustXPrtSNMask_input:
   """ Required : 
   iSNMask
   ds
   """  
   def __init__(self, obj):
      self.iSNMask:str = obj["iSNMask"]
      """  Serial Number Mask Id  """  
      self.ds:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["ds"]
      pass

class ChangeCustXPrtSNMask_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCustXPrtSNOverride_input:
   """ Required : 
   iSNOverride
   ds
   """  
   def __init__(self, obj):
      self.iSNOverride:str = obj["iSNOverride"]
      """  Override Mask  """  
      self.ds:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["ds"]
      pass

class ChangeCustXPrtSNOverride_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCustXPrtXPartNum_input:
   """ Required : 
   iXPartNum
   ds
   """  
   def __init__(self, obj):
      self.iXPartNum:str = obj["iXPartNum"]
      """  Customer Part Number  """  
      self.ds:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["ds"]
      pass

class ChangeCustXPrtXPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeListCustXPrtPartNum_input:
   """ Required : 
   iPartNum
   ds
   sysRowID
   rowType
   """  
   def __init__(self, obj):
      self.iPartNum:str = obj["iPartNum"]
      self.ds:list[Erp_Tablesets_CustomerPartXRefListTableset] = obj["ds"]
      self.sysRowID:str = obj["sysRowID"]
      self.rowType:str = obj["rowType"]
      pass

class ChangeListCustXPrtPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.iPartNum:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_CustomerPartXRefListTableset] = obj["ds"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class ChangeMaskPrefixSuffix_input:
   """ Required : 
   icValue
   icPorC
   ds
   """  
   def __init__(self, obj):
      self.icValue:str = obj["icValue"]
      """  MaskPrefix or MaskSuffix value  """  
      self.icPorC:str = obj["icPorC"]
      """  Which one to check  """  
      self.ds:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["ds"]
      pass

class ChangeMaskPrefixSuffix_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   custNum
   partNum
   xpartNum
   sysRowID
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      self.partNum:str = obj["partNum"]
      self.xpartNum:str = obj["xpartNum"]
      self.sysRowID:str = obj["sysRowID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteByPart_input:
   """ Required : 
   partNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      pass

class DeleteByPart_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CustXPrtListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Our Part number used to identify this part.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number of this part cross reference record  """  
      self.XPartNum:str = obj["XPartNum"]
      """  Part Number that the customer uses to identify the Part.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Customers Part Revision Number.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Description Customer uses to describes the Part.  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNMaskExample:str = obj["SNMaskExample"]
      """  BL-generated example of the serial number mask if SNBaseDataType = Mask.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.SNOverride:bool = obj["SNOverride"]
      """  Override serial mask settings? SN fields are ignored unless this is true.  """  
      self.GlobalCustXPrt:bool = obj["GlobalCustXPrt"]
      """  Marks this CustXPrt as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.WIApplication:str = obj["WIApplication"]
      """  WIApplication  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EDIContainerType:str = obj["EDIContainerType"]
      """  EDIContainerType  """  
      self.ProductionPartNum:str = obj["ProductionPartNum"]
      """  ProductionPartNum  """  
      self.ProductionPartNumIsValid:bool = obj["ProductionPartNumIsValid"]
      """  ProductionPartNumIsValid  """  
      self.ServicePartNum:str = obj["ServicePartNum"]
      """  ServicePartNum  """  
      self.ServicePartNumIsValid:bool = obj["ServicePartNumIsValid"]
      """  ServicePartNumIsValid  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustXPrtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Our Part number used to identify this part.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number of this part cross reference record  """  
      self.XPartNum:str = obj["XPartNum"]
      """  Part Number that the customer uses to identify the Part.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Customers Part Revision Number.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Description Customer uses to describes the Part.  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNMaskExample:str = obj["SNMaskExample"]
      """  BL-generated example of the serial number mask if SNBaseDataType = Mask.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.SNOverride:bool = obj["SNOverride"]
      """  Override serial mask settings? SN fields are ignored unless this is true.  """  
      self.GlobalCustXPrt:bool = obj["GlobalCustXPrt"]
      """  Marks this CustXPrt as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.WIApplication:str = obj["WIApplication"]
      """  WIApplication  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EDIContainerType:str = obj["EDIContainerType"]
      """  EDIContainerType  """  
      self.ProductionPartNum:str = obj["ProductionPartNum"]
      """  ProductionPartNum  """  
      self.ProductionPartNumIsValid:bool = obj["ProductionPartNumIsValid"]
      """  ProductionPartNumIsValid  """  
      self.ServicePartNum:str = obj["ServicePartNum"]
      """  ServicePartNum  """  
      self.ServicePartNumIsValid:bool = obj["ServicePartNumIsValid"]
      """  ServicePartNumIsValid  """  
      self.SNPrefixExampleSuffix:str = obj["SNPrefixExampleSuffix"]
      """  Prefix + Example + Suffix  """  
      self.SuffixLength:int = obj["SuffixLength"]
      """  SuffixLength  """  
      self.PrefixLength:int = obj["PrefixLength"]
      """  PrefixLength  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustomerPartXRefListTableset:
   def __init__(self, obj):
      self.CustXPrtList:list[Erp_Tablesets_CustXPrtListRow] = obj["CustXPrtList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CustomerPartXRefTableset:
   def __init__(self, obj):
      self.CustXPrt:list[Erp_Tablesets_CustXPrtRow] = obj["CustXPrt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCustomerPartXRefTableset:
   def __init__(self, obj):
      self.CustXPrt:list[Erp_Tablesets_CustXPrtRow] = obj["CustXPrt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FindCustPartNum_input:
   """ Required : 
   iCustNum
   partNum
   ds
   """  
   def __init__(self, obj):
      self.iCustNum:int = obj["iCustNum"]
      self.partNum:str = obj["partNum"]
      self.ds:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["ds"]
      pass

class FindCustPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["ds"]
      self.part:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   custNum
   partNum
   xpartNum
   sysRowID
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      self.partNum:str = obj["partNum"]
      self.xpartNum:str = obj["xpartNum"]
      self.sysRowID:str = obj["sysRowID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["returnObj"]
      pass

class GetCustPartXCustPartRef_input:
   """ Required : 
   iCustNum
   partNum
   ds
   """  
   def __init__(self, obj):
      self.iCustNum:int = obj["iCustNum"]
      """  Customer Number  """  
      self.partNum:str = obj["partNum"]
      """  Part Number  """  
      self.ds:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["ds"]
      pass

class GetCustPartXCustPartRef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetCustomerParXRef_input:
   """ Required : 
   iCustNum
   ds
   """  
   def __init__(self, obj):
      self.iCustNum:int = obj["iCustNum"]
      """  Customer Number  """  
      self.ds:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["ds"]
      pass

class GetCustomerParXRef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetListCustPartXCustPartRefByID_input:
   """ Required : 
   CustNum
   CustXPrtRowID
   ds
   """  
   def __init__(self, obj):
      self.CustNum:int = obj["CustNum"]
      self.CustXPrtRowID:str = obj["CustXPrtRowID"]
      """  Customer Part Numbers  """  
      self.ds:list[Erp_Tablesets_CustomerPartXRefListTableset] = obj["ds"]
      pass

class GetListCustPartXCustPartRefByID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustomerPartXRefListTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetListCustPartXCustPartRef_input:
   """ Required : 
   iCustNum
   partNum
   ds
   """  
   def __init__(self, obj):
      self.iCustNum:int = obj["iCustNum"]
      """  Customer Number  """  
      self.partNum:str = obj["partNum"]
      """  Part Number  """  
      self.ds:list[Erp_Tablesets_CustomerPartXRefListTableset] = obj["ds"]
      pass

class GetListCustPartXCustPartRef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustomerPartXRefListTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustomerPartXRefListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCustXPrt_input:
   """ Required : 
   ds
   custNum
   partNum
   xpartNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["ds"]
      self.custNum:int = obj["custNum"]
      self.partNum:str = obj["partNum"]
      self.xpartNum:str = obj["xpartNum"]
      pass

class GetNewCustXPrt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCustXPrt
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCustXPrt:str = obj["whereClauseCustXPrt"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class IsCustXPrtXPartNumInvalid_input:
   """ Required : 
   iXPartNum
   custNum
   """  
   def __init__(self, obj):
      self.iXPartNum:str = obj["iXPartNum"]
      self.custNum:int = obj["custNum"]
      pass

class IsCustXPrtXPartNumInvalid_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class UpdateCustPartOpts_input:
   """ Required : 
   pcCustID
   pcCustPartOpts
   """  
   def __init__(self, obj):
      self.pcCustID:str = obj["pcCustID"]
      """  CustID  """  
      self.pcCustPartOpts:str = obj["pcCustPartOpts"]
      """  CustPartOpts  """  
      pass

class UpdateCustPartOpts_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCustomerPartXRefTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCustomerPartXRefTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustomerPartXRefTableset] = obj["ds"]
      pass

      """  output parameters  """  

