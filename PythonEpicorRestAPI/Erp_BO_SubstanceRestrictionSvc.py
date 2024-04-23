import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.SubstanceRestrictionSvc
# Description: Substance Restriction Type Maintenance
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_SubstanceRestrictions(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SubstanceRestrictions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SubstanceRestrictions
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RestrictionTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/SubstanceRestrictions",headers=creds) as resp:
           return await resp.json()

async def post_SubstanceRestrictions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SubstanceRestrictions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RestrictionTypeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RestrictionTypeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/SubstanceRestrictions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SubstanceRestrictions_Company_RestrictionTypeID(Company, RestrictionTypeID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SubstanceRestriction item
   Description: Calls GetByID to retrieve the SubstanceRestriction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SubstanceRestriction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RestrictionTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/SubstanceRestrictions(" + Company + "," + RestrictionTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SubstanceRestrictions_Company_RestrictionTypeID(Company, RestrictionTypeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SubstanceRestriction for the service
   Description: Calls UpdateExt to update SubstanceRestriction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SubstanceRestriction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RestrictionTypeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/SubstanceRestrictions(" + Company + "," + RestrictionTypeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SubstanceRestrictions_Company_RestrictionTypeID(Company, RestrictionTypeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SubstanceRestriction item
   Description: Call UpdateExt to delete SubstanceRestriction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SubstanceRestriction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/SubstanceRestrictions(" + Company + "," + RestrictionTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SubstanceRestrictions_Company_RestrictionTypeID_RestrictionSubstances(Company, RestrictionTypeID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RestrictionSubstances items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RestrictionSubstances1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RestrictionSubstanceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/SubstanceRestrictions(" + Company + "," + RestrictionTypeID + ")/RestrictionSubstances",headers=creds) as resp:
           return await resp.json()

async def get_SubstanceRestrictions_Company_RestrictionTypeID_RestrictionSubstances_Company_RestrictionTypeID_SubstanceID(Company, RestrictionTypeID, SubstanceID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RestrictionSubstance item
   Description: Calls GetByID to retrieve the RestrictionSubstance item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RestrictionSubstance1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param SubstanceID: Desc: SubstanceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RestrictionSubstanceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/SubstanceRestrictions(" + Company + "," + RestrictionTypeID + ")/RestrictionSubstances(" + Company + "," + RestrictionTypeID + "," + SubstanceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RestrictionSubstances(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RestrictionSubstances items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RestrictionSubstances
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RestrictionSubstanceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/RestrictionSubstances",headers=creds) as resp:
           return await resp.json()

async def post_RestrictionSubstances(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RestrictionSubstances
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RestrictionSubstanceRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RestrictionSubstanceRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/RestrictionSubstances", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RestrictionSubstances_Company_RestrictionTypeID_SubstanceID(Company, RestrictionTypeID, SubstanceID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RestrictionSubstance item
   Description: Calls GetByID to retrieve the RestrictionSubstance item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RestrictionSubstance
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param SubstanceID: Desc: SubstanceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RestrictionSubstanceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/RestrictionSubstances(" + Company + "," + RestrictionTypeID + "," + SubstanceID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RestrictionSubstances_Company_RestrictionTypeID_SubstanceID(Company, RestrictionTypeID, SubstanceID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RestrictionSubstance for the service
   Description: Calls UpdateExt to update RestrictionSubstance. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RestrictionSubstance
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param SubstanceID: Desc: SubstanceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RestrictionSubstanceRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/RestrictionSubstances(" + Company + "," + RestrictionTypeID + "," + SubstanceID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RestrictionSubstances_Company_RestrictionTypeID_SubstanceID(Company, RestrictionTypeID, SubstanceID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RestrictionSubstance item
   Description: Call UpdateExt to delete RestrictionSubstance item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RestrictionSubstance
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param SubstanceID: Desc: SubstanceID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/RestrictionSubstances(" + Company + "," + RestrictionTypeID + "," + SubstanceID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RestrictionTypeListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseRestrictionType, whereClauseRestrictionSubstance, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseRestrictionType=" + whereClauseRestrictionType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRestrictionSubstance=" + whereClauseRestrictionSubstance
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(restrictionTypeID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "restrictionTypeID=" + restrictionTypeID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSubstance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSubstance
   Description: This method should be called when ValidateCompliance change.
   OperationID: OnChangeSubstance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSubstance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSubstance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeThreshold(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeThreshold
   Description: This method should be called when ValidateCompliance change.
   OperationID: OnChangeThreshold
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeThreshold_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeThreshold_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeValidateCompliance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeValidateCompliance
   Description: This method should be called when ValidateCompliance change.
   OperationID: OnChangeValidateCompliance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeValidateCompliance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeValidateCompliance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRestrictionType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRestrictionType
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRestrictionType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRestrictionType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRestrictionType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRestrictionSubstance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRestrictionSubstance
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRestrictionSubstance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRestrictionSubstance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRestrictionSubstance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SubstanceRestrictionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RestrictionSubstanceRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RestrictionSubstanceRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RestrictionTypeListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RestrictionTypeListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RestrictionTypeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RestrictionTypeRow] = obj["value"]
      pass

class Erp_Tablesets_RestrictionSubstanceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.SubstanceID:str = obj["SubstanceID"]
      """  Substance identification.  """  
      self.Threshold:int = obj["Threshold"]
      """  The lowest level threshold allowed for the restriction type.  """  
      self.GlobalRestrictionSubstance:bool = obj["GlobalRestrictionSubstance"]
      """  Marks this RestrictionSubstance as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RestrictionTypeDescription:str = obj["RestrictionTypeDescription"]
      self.SubstanceDescriptionDescription:str = obj["SubstanceDescriptionDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RestrictionTypeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.Description:str = obj["Description"]
      """  Restriction Type Description  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the Restriction Type is inactive and the Roll-Up process will not take it in count.  """  
      self.Compliance:bool = obj["Compliance"]
      """  If checked then compliance for this restriction type will be validated  """  
      self.CheckPurchase:bool = obj["CheckPurchase"]
      """  Validate compliance for purchase order lines and purchase suggestions.  """  
      self.CheckRFQ:bool = obj["CheckRFQ"]
      """  Validate compliance for Request for Quote lines  """  
      self.CheckSOQuote:bool = obj["CheckSOQuote"]
      """  Validate compliance for Sales Order lines and Quote lines  """  
      self.GlobalRestrictionType:bool = obj["GlobalRestrictionType"]
      """  Marks this RestrictionType as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RestrictionTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.Description:str = obj["Description"]
      """  Restriction Type Description  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the Restriction Type is inactive and the Roll-Up process will not take it in count.  """  
      self.Compliance:bool = obj["Compliance"]
      """  If checked then compliance for this restriction type will be validated  """  
      self.CheckPurchase:bool = obj["CheckPurchase"]
      """  Validate compliance for purchase order lines and purchase suggestions.  """  
      self.CheckRFQ:bool = obj["CheckRFQ"]
      """  Validate compliance for Request for Quote lines  """  
      self.CheckSOQuote:bool = obj["CheckSOQuote"]
      """  Validate compliance for Sales Order lines and Quote lines  """  
      self.GlobalRestrictionType:bool = obj["GlobalRestrictionType"]
      """  Marks this RestrictionType as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   restrictionTypeID
   """  
   def __init__(self, obj):
      self.restrictionTypeID:str = obj["restrictionTypeID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_RestrictionSubstanceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.SubstanceID:str = obj["SubstanceID"]
      """  Substance identification.  """  
      self.Threshold:int = obj["Threshold"]
      """  The lowest level threshold allowed for the restriction type.  """  
      self.GlobalRestrictionSubstance:bool = obj["GlobalRestrictionSubstance"]
      """  Marks this RestrictionSubstance as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RestrictionTypeDescription:str = obj["RestrictionTypeDescription"]
      self.SubstanceDescriptionDescription:str = obj["SubstanceDescriptionDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RestrictionTypeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.Description:str = obj["Description"]
      """  Restriction Type Description  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the Restriction Type is inactive and the Roll-Up process will not take it in count.  """  
      self.Compliance:bool = obj["Compliance"]
      """  If checked then compliance for this restriction type will be validated  """  
      self.CheckPurchase:bool = obj["CheckPurchase"]
      """  Validate compliance for purchase order lines and purchase suggestions.  """  
      self.CheckRFQ:bool = obj["CheckRFQ"]
      """  Validate compliance for Request for Quote lines  """  
      self.CheckSOQuote:bool = obj["CheckSOQuote"]
      """  Validate compliance for Sales Order lines and Quote lines  """  
      self.GlobalRestrictionType:bool = obj["GlobalRestrictionType"]
      """  Marks this RestrictionType as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RestrictionTypeListTableset:
   def __init__(self, obj):
      self.RestrictionTypeList:list[Erp_Tablesets_RestrictionTypeListRow] = obj["RestrictionTypeList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RestrictionTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.Description:str = obj["Description"]
      """  Restriction Type Description  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the Restriction Type is inactive and the Roll-Up process will not take it in count.  """  
      self.Compliance:bool = obj["Compliance"]
      """  If checked then compliance for this restriction type will be validated  """  
      self.CheckPurchase:bool = obj["CheckPurchase"]
      """  Validate compliance for purchase order lines and purchase suggestions.  """  
      self.CheckRFQ:bool = obj["CheckRFQ"]
      """  Validate compliance for Request for Quote lines  """  
      self.CheckSOQuote:bool = obj["CheckSOQuote"]
      """  Validate compliance for Sales Order lines and Quote lines  """  
      self.GlobalRestrictionType:bool = obj["GlobalRestrictionType"]
      """  Marks this RestrictionType as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SubstanceRestrictionTableset:
   def __init__(self, obj):
      self.RestrictionType:list[Erp_Tablesets_RestrictionTypeRow] = obj["RestrictionType"]
      self.RestrictionSubstance:list[Erp_Tablesets_RestrictionSubstanceRow] = obj["RestrictionSubstance"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtSubstanceRestrictionTableset:
   def __init__(self, obj):
      self.RestrictionType:list[Erp_Tablesets_RestrictionTypeRow] = obj["RestrictionType"]
      self.RestrictionSubstance:list[Erp_Tablesets_RestrictionSubstanceRow] = obj["RestrictionSubstance"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   restrictionTypeID
   """  
   def __init__(self, obj):
      self.restrictionTypeID:str = obj["restrictionTypeID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SubstanceRestrictionTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SubstanceRestrictionTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SubstanceRestrictionTableset] = obj["returnObj"]
      pass

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
      self.returnObj:list[Erp_Tablesets_RestrictionTypeListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewRestrictionSubstance_input:
   """ Required : 
   ds
   restrictionTypeID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SubstanceRestrictionTableset] = obj["ds"]
      self.restrictionTypeID:str = obj["restrictionTypeID"]
      pass

class GetNewRestrictionSubstance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SubstanceRestrictionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRestrictionType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SubstanceRestrictionTableset] = obj["ds"]
      pass

class GetNewRestrictionType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SubstanceRestrictionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseRestrictionType
   whereClauseRestrictionSubstance
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRestrictionType:str = obj["whereClauseRestrictionType"]
      self.whereClauseRestrictionSubstance:str = obj["whereClauseRestrictionSubstance"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SubstanceRestrictionTableset] = obj["returnObj"]
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

class OnChangeSubstance_input:
   """ Required : 
   validaSubstance
   typeID
   ds
   """  
   def __init__(self, obj):
      self.validaSubstance:str = obj["validaSubstance"]
      """  Valida SubstanceID  """  
      self.typeID:str = obj["typeID"]
      """  Restriction Type  """  
      self.ds:list[Erp_Tablesets_SubstanceRestrictionTableset] = obj["ds"]
      pass

class OnChangeSubstance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SubstanceRestrictionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeThreshold_input:
   """ Required : 
   validaThreshold
   """  
   def __init__(self, obj):
      self.validaThreshold:int = obj["validaThreshold"]
      """  Valida Threshold  """  
      pass

class OnChangeThreshold_output:
   def __init__(self, obj):
      pass

class OnChangeValidateCompliance_input:
   """ Required : 
   checkCompliance
   ds
   """  
   def __init__(self, obj):
      self.checkCompliance:bool = obj["checkCompliance"]
      """  Proposed Compliance.  """  
      self.ds:list[Erp_Tablesets_SubstanceRestrictionTableset] = obj["ds"]
      pass

class OnChangeValidateCompliance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SubstanceRestrictionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSubstanceRestrictionTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSubstanceRestrictionTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SubstanceRestrictionTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SubstanceRestrictionTableset] = obj["ds"]
      pass

      """  output parameters  """  

