import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PriceLstPartsSvc
# Description: The PriceLstParts Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PriceLstParts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PriceLstParts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PriceLstParts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstPartsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PriceLstParts",headers=creds) as resp:
           return await resp.json()

async def post_PriceLstParts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PriceLstParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PriceLstPartsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PriceLstPartsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PriceLstParts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PriceLstParts_Company_ListCode_PartNum_UOMCode(Company, ListCode, PartNum, UOMCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PriceLstPart item
   Description: Calls GetByID to retrieve the PriceLstPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PriceLstPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PriceLstPartsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PriceLstParts(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PriceLstParts_Company_ListCode_PartNum_UOMCode(Company, ListCode, PartNum, UOMCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PriceLstPart for the service
   Description: Calls UpdateExt to update PriceLstPart. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PriceLstPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PriceLstPartsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PriceLstParts(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PriceLstParts_Company_ListCode_PartNum_UOMCode(Company, ListCode, PartNum, UOMCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PriceLstPart item
   Description: Call UpdateExt to delete PriceLstPart item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PriceLstPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PriceLstParts(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_PriceLstParts_Company_ListCode_PartNum_UOMCode_PLPartBrks(Company, ListCode, PartNum, UOMCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PLPartBrks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PLPartBrks1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PLPartBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PriceLstParts(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + ")/PLPartBrks",headers=creds) as resp:
           return await resp.json()

async def get_PriceLstParts_Company_ListCode_PartNum_UOMCode_PLPartBrks_Company_ListCode_PartNum_UOMCode_Quantity(Company, ListCode, PartNum, UOMCode, Quantity, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PLPartBrk item
   Description: Calls GetByID to retrieve the PLPartBrk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PLPartBrk1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param Quantity: Desc: Quantity   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PLPartBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PriceLstParts(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + ")/PLPartBrks(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + "," + Quantity + ")",headers=creds) as resp:
           return await resp.json()

async def get_PLPartBrks(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PLPartBrks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PLPartBrks
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PLPartBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PLPartBrks",headers=creds) as resp:
           return await resp.json()

async def post_PLPartBrks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PLPartBrks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PLPartBrkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PLPartBrkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PLPartBrks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PLPartBrks_Company_ListCode_PartNum_UOMCode_Quantity(Company, ListCode, PartNum, UOMCode, Quantity, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PLPartBrk item
   Description: Calls GetByID to retrieve the PLPartBrk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PLPartBrk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param Quantity: Desc: Quantity   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PLPartBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PLPartBrks(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + "," + Quantity + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PLPartBrks_Company_ListCode_PartNum_UOMCode_Quantity(Company, ListCode, PartNum, UOMCode, Quantity, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PLPartBrk for the service
   Description: Calls UpdateExt to update PLPartBrk. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PLPartBrk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param Quantity: Desc: Quantity   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PLPartBrkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PLPartBrks(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + "," + Quantity + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PLPartBrks_Company_ListCode_PartNum_UOMCode_Quantity(Company, ListCode, PartNum, UOMCode, Quantity, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PLPartBrk item
   Description: Call UpdateExt to delete PLPartBrk item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PLPartBrk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/PLPartBrks(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + "," + Quantity + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstPartsListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePriceLstParts, whereClausePLPartBrk, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePriceLstParts=" + whereClausePriceLstParts
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePLPartBrk=" + whereClausePLPartBrk
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(listCode, partNum, uoMCode, epicorHeaders = None):
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
   params += "partNum=" + partNum
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetListFromSelectedKeys(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListFromSelectedKeys
   Description: This methods will return all of the PriceLstParts records which will be a subset
of the PriceLstParts records that meet the selection criteria.  This method will try
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsFromSelectedKeys(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsFromSelectedKeys
   Description: This methods will return all of the PriceLstParts records which will be a subset
of the PriceLstParts records that meet the selection criteria.  This method will try
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPriceLstParts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPriceLstParts
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPriceLstParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPriceLstParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPriceLstParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPLPartBrk(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPLPartBrk
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPLPartBrk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPLPartBrk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPLPartBrk_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstPartsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PLPartBrkRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PLPartBrkRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstPartsListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PriceLstPartsListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstPartsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PriceLstPartsRow] = obj["value"]
      pass

class Erp_Tablesets_PLPartBrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """   Unique set of characters entered by the user to identify
the Price List master within the company.  """  
      self.PartNum:str = obj["PartNum"]
      """  Descriptive code assigned by the user to uniquely identify a Part master. Can't be blank.  """  
      self.Quantity:int = obj["Quantity"]
      """  The price break quantity  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The Discount Percent that is to be given for this price break quantity. Do not allow both a discount percent and unit price for the same quantity break to be non-zero or both of them to be zero.  One must be entered but not both.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  The "Flat Unit Price" that is to be given for this price break quantity. Order entry will use this value as an override to the unit price that is found in the part master.  """  
      self.UOMCode:str = obj["UOMCode"]
      """   Unit of Measure code of the part price list break.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPLPartBrk:bool = obj["GlobalPLPartBrk"]
      """  Marks this PLPartBrk as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RadioButtonValue:str = obj["RadioButtonValue"]
      """  Value of radio button. (D or P)  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.Comments_c:str = obj["Comments_c"]
      pass

class Erp_Tablesets_PriceLstPartsListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  PriceLst.ListCode value of the price list that this record is related to.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part.PartNum value of the Part that this record is related to.  """  
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
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak2:int = obj["QtyBreak2"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak3:int = obj["QtyBreak3"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak4:int = obj["QtyBreak4"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak5:int = obj["QtyBreak5"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
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
      """   Unit of Measure code of the part price list.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPriceLstParts:bool = obj["GlobalPriceLstParts"]
      """  Marks this PriceLstParts as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartSalesUM:str = obj["PartSalesUM"]
      """  Part sales unit of measure  """  
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      """  Part selling factor  """  
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      """  Part price per code  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part description  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      """  Description of the price list.  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceLstPartsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  PriceLst.ListCode value of the price list that this record is related to.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part.PartNum value of the Part that this record is related to.  """  
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
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak2:int = obj["QtyBreak2"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak3:int = obj["QtyBreak3"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak4:int = obj["QtyBreak4"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak5:int = obj["QtyBreak5"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
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
      """   Unit of Measure code of the part price list.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPriceLstParts:bool = obj["GlobalPriceLstParts"]
      """  Marks this PriceLstParts as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartSalesUM:str = obj["PartSalesUM"]
      """  Part sales unit of measure  """  
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      """  Part selling factor  """  
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      """  Part price per code  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part description  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.BitFlag:int = obj["BitFlag"]
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   listCode
   partNum
   uoMCode
   """  
   def __init__(self, obj):
      self.listCode:str = obj["listCode"]
      self.partNum:str = obj["partNum"]
      self.uoMCode:str = obj["uoMCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PLPartBrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """   Unique set of characters entered by the user to identify
the Price List master within the company.  """  
      self.PartNum:str = obj["PartNum"]
      """  Descriptive code assigned by the user to uniquely identify a Part master. Can't be blank.  """  
      self.Quantity:int = obj["Quantity"]
      """  The price break quantity  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The Discount Percent that is to be given for this price break quantity. Do not allow both a discount percent and unit price for the same quantity break to be non-zero or both of them to be zero.  One must be entered but not both.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  The "Flat Unit Price" that is to be given for this price break quantity. Order entry will use this value as an override to the unit price that is found in the part master.  """  
      self.UOMCode:str = obj["UOMCode"]
      """   Unit of Measure code of the part price list break.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPLPartBrk:bool = obj["GlobalPLPartBrk"]
      """  Marks this PLPartBrk as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RadioButtonValue:str = obj["RadioButtonValue"]
      """  Value of radio button. (D or P)  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.Comments_c:str = obj["Comments_c"]
      pass

class Erp_Tablesets_PriceLstPartsListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  PriceLst.ListCode value of the price list that this record is related to.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part.PartNum value of the Part that this record is related to.  """  
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
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak2:int = obj["QtyBreak2"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak3:int = obj["QtyBreak3"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak4:int = obj["QtyBreak4"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak5:int = obj["QtyBreak5"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
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
      """   Unit of Measure code of the part price list.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPriceLstParts:bool = obj["GlobalPriceLstParts"]
      """  Marks this PriceLstParts as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartSalesUM:str = obj["PartSalesUM"]
      """  Part sales unit of measure  """  
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      """  Part selling factor  """  
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      """  Part price per code  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part description  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      """  Description of the price list.  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceLstPartsListTableset:
   def __init__(self, obj):
      self.PriceLstPartsList:list[Erp_Tablesets_PriceLstPartsListRow] = obj["PriceLstPartsList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PriceLstPartsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  PriceLst.ListCode value of the price list that this record is related to.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part.PartNum value of the Part that this record is related to.  """  
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
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak2:int = obj["QtyBreak2"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak3:int = obj["QtyBreak3"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak4:int = obj["QtyBreak4"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak5:int = obj["QtyBreak5"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
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
      """   Unit of Measure code of the part price list.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPriceLstParts:bool = obj["GlobalPriceLstParts"]
      """  Marks this PriceLstParts as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartSalesUM:str = obj["PartSalesUM"]
      """  Part sales unit of measure  """  
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      """  Part selling factor  """  
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      """  Part price per code  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part description  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.BitFlag:int = obj["BitFlag"]
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceLstPartsTableset:
   def __init__(self, obj):
      self.PriceLstParts:list[Erp_Tablesets_PriceLstPartsRow] = obj["PriceLstParts"]
      self.PLPartBrk:list[Erp_Tablesets_PLPartBrkRow] = obj["PLPartBrk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPriceLstPartsTableset:
   def __init__(self, obj):
      self.PriceLstParts:list[Erp_Tablesets_PriceLstPartsRow] = obj["PriceLstParts"]
      self.PLPartBrk:list[Erp_Tablesets_PLPartBrkRow] = obj["PLPartBrk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   listCode
   partNum
   uoMCode
   """  
   def __init__(self, obj):
      self.listCode:str = obj["listCode"]
      self.partNum:str = obj["partNum"]
      self.uoMCode:str = obj["uoMCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PriceLstPartsTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PriceLstPartsTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PriceLstPartsTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_PriceLstPartsListTableset] = obj["ds"]
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetListFromSelectedKeys_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstPartsListTableset] = obj["ds"]
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
      self.returnObj:list[Erp_Tablesets_PriceLstPartsListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPLPartBrk_input:
   """ Required : 
   ds
   listCode
   partNum
   uoMCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstPartsTableset] = obj["ds"]
      self.listCode:str = obj["listCode"]
      self.partNum:str = obj["partNum"]
      self.uoMCode:str = obj["uoMCode"]
      pass

class GetNewPLPartBrk_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstPartsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPriceLstParts_input:
   """ Required : 
   ds
   listCode
   partNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstPartsTableset] = obj["ds"]
      self.listCode:str = obj["listCode"]
      self.partNum:str = obj["partNum"]
      pass

class GetNewPriceLstParts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstPartsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsFromSelectedKeys_input:
   """ Required : 
   ds
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstPartsTableset] = obj["ds"]
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetRowsFromSelectedKeys_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstPartsTableset] = obj["ds"]
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePriceLstParts
   whereClausePLPartBrk
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePriceLstParts:str = obj["whereClausePriceLstParts"]
      self.whereClausePLPartBrk:str = obj["whereClausePLPartBrk"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PriceLstPartsTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtPriceLstPartsTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPriceLstPartsTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstPartsTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstPartsTableset] = obj["ds"]
      pass

      """  output parameters  """  

