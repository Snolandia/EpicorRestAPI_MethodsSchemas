import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PriceLstGroupsSvc
# Description: The PriceLstGroups Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PriceLstGroups(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PriceLstGroups items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PriceLstGroups
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstGroupsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PriceLstGroups",headers=creds) as resp:
           return await resp.json()

async def post_PriceLstGroups(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PriceLstGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PriceLstGroupsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PriceLstGroupsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PriceLstGroups", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PriceLstGroups_Company_ListCode_ProdCode_UOMCode(Company, ListCode, ProdCode, UOMCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PriceLstGroup item
   Description: Calls GetByID to retrieve the PriceLstGroup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PriceLstGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param ProdCode: Desc: ProdCode   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PriceLstGroupsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PriceLstGroups(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PriceLstGroups_Company_ListCode_ProdCode_UOMCode(Company, ListCode, ProdCode, UOMCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PriceLstGroup for the service
   Description: Calls UpdateExt to update PriceLstGroup. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PriceLstGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param ProdCode: Desc: ProdCode   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PriceLstGroupsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PriceLstGroups(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PriceLstGroups_Company_ListCode_ProdCode_UOMCode(Company, ListCode, ProdCode, UOMCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PriceLstGroup item
   Description: Call UpdateExt to delete PriceLstGroup item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PriceLstGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param ProdCode: Desc: ProdCode   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PriceLstGroups(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_PriceLstGroups_Company_ListCode_ProdCode_UOMCode_PLGrupBrks(Company, ListCode, ProdCode, UOMCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PLGrupBrks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PLGrupBrks1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param ProdCode: Desc: ProdCode   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PLGrupBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PriceLstGroups(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + ")/PLGrupBrks",headers=creds) as resp:
           return await resp.json()

async def get_PriceLstGroups_Company_ListCode_ProdCode_UOMCode_PLGrupBrks_Company_ListCode_ProdCode_UOMCode_Quantity(Company, ListCode, ProdCode, UOMCode, Quantity, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PLGrupBrk item
   Description: Calls GetByID to retrieve the PLGrupBrk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PLGrupBrk1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param ProdCode: Desc: ProdCode   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param Quantity: Desc: Quantity   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PLGrupBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PriceLstGroups(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + ")/PLGrupBrks(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + "," + Quantity + ")",headers=creds) as resp:
           return await resp.json()

async def get_PLGrupBrks(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PLGrupBrks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PLGrupBrks
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PLGrupBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PLGrupBrks",headers=creds) as resp:
           return await resp.json()

async def post_PLGrupBrks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PLGrupBrks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PLGrupBrkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PLGrupBrkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PLGrupBrks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PLGrupBrks_Company_ListCode_ProdCode_UOMCode_Quantity(Company, ListCode, ProdCode, UOMCode, Quantity, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PLGrupBrk item
   Description: Calls GetByID to retrieve the PLGrupBrk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PLGrupBrk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param ProdCode: Desc: ProdCode   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param Quantity: Desc: Quantity   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PLGrupBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PLGrupBrks(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + "," + Quantity + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PLGrupBrks_Company_ListCode_ProdCode_UOMCode_Quantity(Company, ListCode, ProdCode, UOMCode, Quantity, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PLGrupBrk for the service
   Description: Calls UpdateExt to update PLGrupBrk. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PLGrupBrk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param ProdCode: Desc: ProdCode   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param Quantity: Desc: Quantity   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PLGrupBrkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PLGrupBrks(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + "," + Quantity + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PLGrupBrks_Company_ListCode_ProdCode_UOMCode_Quantity(Company, ListCode, ProdCode, UOMCode, Quantity, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PLGrupBrk item
   Description: Call UpdateExt to delete PLGrupBrk item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PLGrupBrk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param ProdCode: Desc: ProdCode   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param Quantity: Desc: Quantity   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/PLGrupBrks(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + "," + Quantity + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstGroupsListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePriceLstGroups, whereClausePLGrupBrk, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClausePriceLstGroups=" + whereClausePriceLstGroups
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePLGrupBrk=" + whereClausePLGrupBrk
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(listCode, prodCode, uoMCode, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "listCode=" + listCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "prodCode=" + prodCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "uoMCode=" + uoMCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetListFromSelectedKeys(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListFromSelectedKeys
   Description: This methods will return all of the PriceLstGroups records which will be a subset
of the PriceLstGroups records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method.
   OperationID: GetListFromSelectedKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListFromSelectedKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListFromSelectedKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsFromSelectedKeys(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsFromSelectedKeys
   Description: This methods will return all of the PriceLstGroups records which will be a subset
of the PriceLstGroups records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method.
   OperationID: GetRowsFromSelectedKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsFromSelectedKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsFromSelectedKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrencyCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrencyCode
   OperationID: GetCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPriceLstGroups(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPriceLstGroups
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPriceLstGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPriceLstGroups_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPriceLstGroups_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPLGrupBrk(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPLGrupBrk
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPLGrupBrk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPLGrupBrk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPLGrupBrk_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstGroupsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PLGrupBrkRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PLGrupBrkRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstGroupsListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PriceLstGroupsListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstGroupsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PriceLstGroupsRow] = obj["value"]
      pass

class Erp_Tablesets_PLGrupBrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  Unique set of characters entered by the user to identify the Price List master within the company.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Descriptive code assigned by the user to uniquely identify a Product Group master.  """  
      self.Quantity:int = obj["Quantity"]
      """  The price break quantity  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The Discount Percent that is to be given for this price break quantity. Do not allow both a discount percent and unit price for the same quantity break .  to be non-zero or both of them to be zero.  One must be entered but not both.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  The "Flat Unit Price" that is to be given for this price break quantity.  """  
      self.UOMCode:str = obj["UOMCode"]
      """   Unit of Measure code of the group price list break.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPLGrupBrk:bool = obj["GlobalPLGrupBrk"]
      """  Marks this PLGrupBrk as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RadioButtonValue:str = obj["RadioButtonValue"]
      """  Value of radio button (P or D)  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceLstGroupsListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  PriceLst.ListCode value of the price list that this record is related to.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdGrup.ProdCode value of the Product Group that this record is related to.  """  
      self.BasePrice:int = obj["BasePrice"]
      """  Base Price for this product group against which the quantity breaks will be applied. Can be zero.  """  
      self.DiscountPercent1:int = obj["DiscountPercent1"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent2:int = obj["DiscountPercent2"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent3:int = obj["DiscountPercent3"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent4:int = obj["DiscountPercent4"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent5:int = obj["DiscountPercent5"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.QtyBreak1:int = obj["QtyBreak1"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak2:int = obj["QtyBreak2"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak3:int = obj["QtyBreak3"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak4:int = obj["QtyBreak4"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak5:int = obj["QtyBreak5"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.UnitPrice1:int = obj["UnitPrice1"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice2:int = obj["UnitPrice2"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice3:int = obj["UnitPrice3"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice4:int = obj["UnitPrice4"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice5:int = obj["UnitPrice5"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.CommentText:str = obj["CommentText"]
      """  Additional comments that will be used as a default for customer price lists.  """  
      self.UOMCode:str = obj["UOMCode"]
      """   Unit of Measure code of the Price List Group.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPriceLstGroups:bool = obj["GlobalPriceLstGroups"]
      """  Marks this PriceLstGroups as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProdGrpDescription:str = obj["ProdGrpDescription"]
      """  Product group description  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      """  Description of the price list.  """  
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      """  Full description of Product Group.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceLstGroupsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  PriceLst.ListCode value of the price list that this record is related to.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdGrup.ProdCode value of the Product Group that this record is related to.  """  
      self.BasePrice:int = obj["BasePrice"]
      """  Base Price for this product group against which the quantity breaks will be applied. Can be zero.  """  
      self.DiscountPercent1:int = obj["DiscountPercent1"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent2:int = obj["DiscountPercent2"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent3:int = obj["DiscountPercent3"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent4:int = obj["DiscountPercent4"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent5:int = obj["DiscountPercent5"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.QtyBreak1:int = obj["QtyBreak1"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak2:int = obj["QtyBreak2"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak3:int = obj["QtyBreak3"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak4:int = obj["QtyBreak4"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak5:int = obj["QtyBreak5"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.UnitPrice1:int = obj["UnitPrice1"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice2:int = obj["UnitPrice2"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice3:int = obj["UnitPrice3"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice4:int = obj["UnitPrice4"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice5:int = obj["UnitPrice5"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.CommentText:str = obj["CommentText"]
      """  Additional comments that will be used as a default for customer price lists.  """  
      self.UOMCode:str = obj["UOMCode"]
      """   Unit of Measure code of the Price List Group.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPriceLstGroups:bool = obj["GlobalPriceLstGroups"]
      """  Marks this PriceLstGroups as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProdGrpDescription:str = obj["ProdGrpDescription"]
      """  Product group description  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   listCode
   prodCode
   uoMCode
   """  
   def __init__(self, obj):
      self.listCode:str = obj["listCode"]
      self.prodCode:str = obj["prodCode"]
      self.uoMCode:str = obj["uoMCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PLGrupBrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  Unique set of characters entered by the user to identify the Price List master within the company.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Descriptive code assigned by the user to uniquely identify a Product Group master.  """  
      self.Quantity:int = obj["Quantity"]
      """  The price break quantity  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The Discount Percent that is to be given for this price break quantity. Do not allow both a discount percent and unit price for the same quantity break .  to be non-zero or both of them to be zero.  One must be entered but not both.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  The "Flat Unit Price" that is to be given for this price break quantity.  """  
      self.UOMCode:str = obj["UOMCode"]
      """   Unit of Measure code of the group price list break.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPLGrupBrk:bool = obj["GlobalPLGrupBrk"]
      """  Marks this PLGrupBrk as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RadioButtonValue:str = obj["RadioButtonValue"]
      """  Value of radio button (P or D)  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceLstGroupsListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  PriceLst.ListCode value of the price list that this record is related to.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdGrup.ProdCode value of the Product Group that this record is related to.  """  
      self.BasePrice:int = obj["BasePrice"]
      """  Base Price for this product group against which the quantity breaks will be applied. Can be zero.  """  
      self.DiscountPercent1:int = obj["DiscountPercent1"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent2:int = obj["DiscountPercent2"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent3:int = obj["DiscountPercent3"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent4:int = obj["DiscountPercent4"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent5:int = obj["DiscountPercent5"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.QtyBreak1:int = obj["QtyBreak1"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak2:int = obj["QtyBreak2"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak3:int = obj["QtyBreak3"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak4:int = obj["QtyBreak4"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak5:int = obj["QtyBreak5"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.UnitPrice1:int = obj["UnitPrice1"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice2:int = obj["UnitPrice2"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice3:int = obj["UnitPrice3"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice4:int = obj["UnitPrice4"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice5:int = obj["UnitPrice5"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.CommentText:str = obj["CommentText"]
      """  Additional comments that will be used as a default for customer price lists.  """  
      self.UOMCode:str = obj["UOMCode"]
      """   Unit of Measure code of the Price List Group.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPriceLstGroups:bool = obj["GlobalPriceLstGroups"]
      """  Marks this PriceLstGroups as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProdGrpDescription:str = obj["ProdGrpDescription"]
      """  Product group description  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      """  Description of the price list.  """  
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      """  Full description of Product Group.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceLstGroupsListTableset:
   def __init__(self, obj):
      self.PriceLstGroupsList:list[Erp_Tablesets_PriceLstGroupsListRow] = obj["PriceLstGroupsList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PriceLstGroupsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  PriceLst.ListCode value of the price list that this record is related to.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdGrup.ProdCode value of the Product Group that this record is related to.  """  
      self.BasePrice:int = obj["BasePrice"]
      """  Base Price for this product group against which the quantity breaks will be applied. Can be zero.  """  
      self.DiscountPercent1:int = obj["DiscountPercent1"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent2:int = obj["DiscountPercent2"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent3:int = obj["DiscountPercent3"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent4:int = obj["DiscountPercent4"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent5:int = obj["DiscountPercent5"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.QtyBreak1:int = obj["QtyBreak1"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak2:int = obj["QtyBreak2"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak3:int = obj["QtyBreak3"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak4:int = obj["QtyBreak4"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak5:int = obj["QtyBreak5"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.UnitPrice1:int = obj["UnitPrice1"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice2:int = obj["UnitPrice2"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice3:int = obj["UnitPrice3"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice4:int = obj["UnitPrice4"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice5:int = obj["UnitPrice5"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.CommentText:str = obj["CommentText"]
      """  Additional comments that will be used as a default for customer price lists.  """  
      self.UOMCode:str = obj["UOMCode"]
      """   Unit of Measure code of the Price List Group.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPriceLstGroups:bool = obj["GlobalPriceLstGroups"]
      """  Marks this PriceLstGroups as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProdGrpDescription:str = obj["ProdGrpDescription"]
      """  Product group description  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceLstGroupsTableset:
   def __init__(self, obj):
      self.PriceLstGroups:list[Erp_Tablesets_PriceLstGroupsRow] = obj["PriceLstGroups"]
      self.PLGrupBrk:list[Erp_Tablesets_PLGrupBrkRow] = obj["PLGrupBrk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPriceLstGroupsTableset:
   def __init__(self, obj):
      self.PriceLstGroups:list[Erp_Tablesets_PriceLstGroupsRow] = obj["PriceLstGroups"]
      self.PLGrupBrk:list[Erp_Tablesets_PLGrupBrkRow] = obj["PLGrupBrk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   listCode
   prodCode
   uoMCode
   """  
   def __init__(self, obj):
      self.listCode:str = obj["listCode"]
      self.prodCode:str = obj["prodCode"]
      self.uoMCode:str = obj["uoMCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PriceLstGroupsTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PriceLstGroupsTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PriceLstGroupsTableset] = obj["returnObj"]
      pass

class GetCurrencyCode_input:
   """ Required : 
   ipListCode
   """  
   def __init__(self, obj):
      self.ipListCode:str = obj["ipListCode"]
      pass

class GetCurrencyCode_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetListFromSelectedKeys_input:
   """ Required : 
   ds
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstGroupsListTableset] = obj["ds"]
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetListFromSelectedKeys_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstGroupsListTableset] = obj["ds"]
      self.morePages:bool = obj["morePages"]
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
      self.returnObj:list[Erp_Tablesets_PriceLstGroupsListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPLGrupBrk_input:
   """ Required : 
   ds
   listCode
   prodCode
   uoMCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstGroupsTableset] = obj["ds"]
      self.listCode:str = obj["listCode"]
      self.prodCode:str = obj["prodCode"]
      self.uoMCode:str = obj["uoMCode"]
      pass

class GetNewPLGrupBrk_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstGroupsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPriceLstGroups_input:
   """ Required : 
   ds
   listCode
   prodCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstGroupsTableset] = obj["ds"]
      self.listCode:str = obj["listCode"]
      self.prodCode:str = obj["prodCode"]
      pass

class GetNewPriceLstGroups_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstGroupsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsFromSelectedKeys_input:
   """ Required : 
   ds
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstGroupsTableset] = obj["ds"]
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetRowsFromSelectedKeys_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstGroupsTableset] = obj["ds"]
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePriceLstGroups
   whereClausePLGrupBrk
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePriceLstGroups:str = obj["whereClausePriceLstGroups"]
      self.whereClausePLGrupBrk:str = obj["whereClausePLGrupBrk"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PriceLstGroupsTableset] = obj["returnObj"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPriceLstGroupsTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPriceLstGroupsTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstGroupsTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstGroupsTableset] = obj["ds"]
      pass

      """  output parameters  """  

